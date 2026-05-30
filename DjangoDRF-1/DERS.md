# Django REST Framework — 1-ci Dərs
## Blog API: Sıfırdan CRUD

---

# REST API nədir?

Siz Django MVT ilə sayt yazdınız. MVT-də view HTML qaytarır:

```python
# MVT — yalnız browser oxuya bilir
def post_list(request):
    posts = Post.objects.all()
    return render(request, 'posts.html', {'posts': posts})
```

REST API-da view **JSON** qaytarır:

```python
# REST API — hər şey oxuya bilir: browser, mobil app, React, Flutter...
def post_list(request):
    posts = Post.objects.all()
    serializer = PostSerializer(posts, many=True)
    return Response(serializer.data)
```

**Niyə JSON?**
JSON universal dildir. İstər iPhone app, istər Android, istər React — hamısı JSON oxuya bilir.

---

## HTTP Metodları

| Metod | Nə edir | URL nümunəsi |
|---|---|---|
| `GET` | Məlumat oxu | `GET /api/posts/` |
| `POST` | Yeni məlumat yarat | `POST /api/posts/` |
| `PUT` | Məlumatı tam yenilə | `PUT /api/posts/1/` |
| `PATCH` | Məlumatı hissəli yenilə | `PATCH /api/posts/1/` |
| `DELETE` | Məlumatı sil | `DELETE /api/posts/1/` |

## Status Kodları

```
200 OK           → Uğurlu GET
201 Created      → Uğurlu POST (yeni şey yarandı)
204 No Content   → Uğurlu DELETE (qaytaracaq şey yoxdur)
400 Bad Request  → Göndərdiyiniz data yanlışdır
404 Not Found    → Axtardığınız şey tapılmadı
```

---

# Model

```python
# blog/models.py

class Category(models.Model):
    name = models.CharField(max_length=100)

class Post(models.Model):
    title      = models.CharField(max_length=200)
    content    = models.TextField()
    category   = models.ForeignKey(Category, related_name='posts', on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    is_published = models.BooleanField(default=False)
```

Django MVT-dən tanışdır. DRF-də model eynidir — dəyişmir.

---

# Serializer

## Serializer nədir?

MVT-də **Form** var idi — formdan gələn datanı yoxlayır, modeli doldururdu.
DRF-də **Serializer** var — JSON-dan gələn datanı yoxlayır, modeli doldurur. Və əksinə.

```
Python obyekti  ──→  Serializer  ──→  JSON     (Serialization)
JSON            ──→  Serializer  ──→  Python   (Deserialization)
```

## Serializer faylı

```python
# blog/serializers.py

class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = '__all__'      # bütün sahələri daxil et
```

```python
class PostSerializer(serializers.ModelSerializer):
    class Meta:
        model = Post
        fields = '__all__'
        read_only_fields = ['created_at', 'updated_at']
        #                    ↑
        #   Bu sahələri user göndərə bilməz.
        #   Server özü doldurur (auto_now_add, auto_now).
```

```python
class PostDetailSerializer(serializers.ModelSerializer):
    category = CategorySerializer(read_only=True)
    #          ↑ nested serializer — GET-də category ID deyil, tam obyekt gəlir:
    #          "category": {"id": 1, "name": "Tech"}

    category_id = serializers.PrimaryKeyRelatedField(
        queryset=Category.objects.all(), source='category', write_only=True
    )
    #   ↑ POST/PUT-da yalnız category ID göndəririk: "category_id": 1
    #   write_only=True — GET cavabında görünmür, yalnız POST/PUT-da qəbul edir

    class Meta:
        model = Post
        fields = '__all__'
        read_only_fields = ['created_at', 'updated_at']
```

**Niyə iki ayrı serializer?**
- `PostSerializer` — list üçün (sadə, sürətli)
- `PostDetailSerializer` — detail üçün (tam məlumat, nested)

---

# Mərhələ 1 — `@api_view` (Function-Based View)

DRF-ə ən sadə giriş nöqtəsi. Django MVT-dəki adi funksiyaya çox bənzəyir.

```python
# blog/views_fbv.py

@api_view(['GET', 'POST'])
#          ↑ Bu endpoint yalnız GET və POST qəbul edir.
#            Başqa metod gəlsə DRF avtomatik 405 Method Not Allowed qaytarır.
def post_list(request):

    if request.method == 'GET':
        posts = Post.objects.all()
        serializer = PostSerializer(posts, many=True)
        #                                  ↑
        #   many=True — bir obyekt deyil, siyahı serialize edirik.
        #   Unutsan → TypeError: 'QuerySet' is not JSON serializable
        return Response(serializer.data)

    # POST
    serializer = PostSerializer(data=request.data)
    #                                 ↑
    #   request.data — gələn JSON-u Python dict-ə çevirir.
    #   MVT-dəki request.POST kimidir.

    if serializer.is_valid():
        #          ↑ Validation yoxlayır:
        #            - Sahələr varmı?
        #            - Tipləri düzgündürmü?
        #            - FK mövcuddurmu?
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)

    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    #               ↑ Nə yanlışdır? Məsələn:
    #               {"title": ["This field is required."]}
```

---

```python
@api_view(['GET', 'PUT', 'DELETE'])
def post_detail(request, pk):

    try:
        post = Post.objects.get(pk=pk)
    except Post.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)
    #   ↑ Tapılmasa — 404 qaytar. Heç nə qaytarmırıq, sadəcə status kodu.

    if request.method == 'GET':
        serializer = PostDetailSerializer(post)
        #                                  ↑ instance verirик — many=True lazım deyil
        return Response(serializer.data)

    if request.method == 'PUT':
        serializer = PostSerializer(post, data=request.data)
        #                           ↑     ↑
        #                        instance  yeni data
        #   İki arqument = UPDATE əməliyyatı.
        #   Bir arqument = CREATE əməliyyatı.
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    # DELETE
    post.delete()
    return Response(status=status.HTTP_204_NO_CONTENT)
    #   ↑ 204 — "Silindi, qaytaracaq şey yoxdur."
```

## Endpointlər (Mərhələ 1)

```
GET    /api/posts/      → bütün postlar
POST   /api/posts/      → yeni post yarat
GET    /api/posts/1/    → 1 nömrəli post
PUT    /api/posts/1/    → 1 nömrəli postu yenilə
DELETE /api/posts/1/    → 1 nömrəli postu sil
```

---

# Mərhələ 2 — `APIView` (Class-Based View)

FBV ilə eyni məntiqi sinif şəklində yazırıq.
`if request.method == 'GET':` əvəzinə ayrı metodlar.

```python
# blog/views_cbv.py

class PostListAPIView(APIView):

    def get(self, request):
    #   ↑ GET gəldikdə bu metod çağırılır. Heç bir if lazım deyil.
        posts = Post.objects.all()
        serializer = PostSerializer(posts, many=True)
        return Response(serializer.data)

    def post(self, request):
    #   ↑ POST gəldikdə bu metod çağırılır.
        serializer = PostSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
```

---

```python
class PostDetailAPIView(APIView):

    def get_object(self, pk):
    #   ↑ Köməkçi metod — hər metodda (get, put, delete) eyni
    #     try/except yazmamaq üçün bir yerə topladıq.
        try:
            return Post.objects.get(pk=pk)
        except Post.DoesNotExist:
            return None

    def get(self, request, pk):
        post = self.get_object(pk)
        if not post:
            return Response(status=status.HTTP_404_NOT_FOUND)
        serializer = PostDetailSerializer(post)
        return Response(serializer.data)

    def put(self, request, pk):
        post = self.get_object(pk)
        if not post:
            return Response(status=status.HTTP_404_NOT_FOUND)
        serializer = PostSerializer(post, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk):
        post = self.get_object(pk)
        if not post:
            return Response(status=status.HTTP_404_NOT_FOUND)
        post.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
```

## FBV vs CBV Müqayisəsi

| | FBV (`@api_view`) | CBV (`APIView`) |
|---|---|---|
| Struktur | Bir funksiya | Sinif + metodlar |
| HTTP metod ayrımı | `if request.method ==` | Ayrı metodlar (`def get`, `def post`) |
| Kod həcmi | Eyni | Eyni |
| Oxunaqlılıq | Sadə, birbaşa | Daha strukturlu |
| Nə vaxt? | Sadə, tez yazılacaq view | Daha mürəkkəb məntiqdə |

> **Vacib:** FBV və CBV funksionallıq baxımından eynidir. Yalnız yazılış tərzi fərqlidir.

---

# Mərhələ 3 — Generic Views

DRF-in ən güclü tərəfi. Standart CRUD əməliyyatları üçün artıq hazır sinifləri var.

```python
# blog/views_generic.py

class PostListCreateView(generics.ListCreateAPIView):
#                                 ↑
#   Bu bir sinif adı deyil — DRF-in hazır sinifidir.
#   İçərisində get() və post() metodları artıq yazılıb.
#   Siz yalnız iki şey deyirsiniz:

    queryset = Post.objects.all()
    #   ↑ hansı datadan istifadə et?

    serializer_class = PostSerializer
    #   ↑ datanı hansı serializer ilə çevir?
```

```python
class PostDetailView(generics.RetrieveUpdateDestroyAPIView):
#                                ↑
#   get (detail) + put + patch + delete — hamısı birlikdə.

    queryset = Post.objects.all()
    serializer_class = PostDetailSerializer
```

**Cəmi 3 sətir kod ilə tam CRUD.**

## Hazır Generic View Sinifləri

```
ListAPIView                   → GET  (siyahı)
CreateAPIView                 → POST
ListCreateAPIView             → GET + POST

RetrieveAPIView               → GET  (tək obyekt)
UpdateAPIView                 → PUT + PATCH
DestroyAPIView                → DELETE
RetrieveUpdateDestroyAPIView  → GET + PUT + PATCH + DELETE
```

## 3 Mərhələnin Kod Müqayisəsi

**FBV — `post_list` + `post_detail`:**
```python
@api_view(['GET', 'POST'])
def post_list(request):
    if request.method == 'GET':
        posts = Post.objects.all()
        serializer = PostSerializer(posts, many=True)
        return Response(serializer.data)
    serializer = PostSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET', 'PUT', 'DELETE'])
def post_detail(request, pk):
    try:
        post = Post.objects.get(pk=pk)
    except Post.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)
    if request.method == 'GET':
        return Response(PostDetailSerializer(post).data)
    if request.method == 'PUT':
        s = PostSerializer(post, data=request.data)
        if s.is_valid():
            s.save()
            return Response(s.data)
        return Response(s.errors, status=400)
    post.delete()
    return Response(status=204)
# ≈ 22 sətir
```

**CBV — `PostListAPIView` + `PostDetailAPIView`:**
```python
class PostListAPIView(APIView):
    def get(self, request):
        return Response(PostSerializer(Post.objects.all(), many=True).data)
    def post(self, request):
        s = PostSerializer(data=request.data)
        if s.is_valid():
            s.save()
            return Response(s.data, status=201)
        return Response(s.errors, status=400)

class PostDetailAPIView(APIView):
    def get_object(self, pk):
        try:
            return Post.objects.get(pk=pk)
        except Post.DoesNotExist:
            return None
    def get(self, request, pk):
        post = self.get_object(pk)
        if not post: return Response(status=404)
        return Response(PostDetailSerializer(post).data)
    def put(self, request, pk):
        post = self.get_object(pk)
        if not post: return Response(status=404)
        s = PostSerializer(post, data=request.data)
        if s.is_valid():
            s.save()
            return Response(s.data)
        return Response(s.errors, status=400)
    def delete(self, request, pk):
        post = self.get_object(pk)
        if not post: return Response(status=404)
        post.delete()
        return Response(status=204)
# ≈ 25 sətir
```

**Generic — `PostListCreateView` + `PostDetailView`:**
```python
class PostListCreateView(generics.ListCreateAPIView):
    queryset = Post.objects.all()
    serializer_class = PostSerializer

class PostDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Post.objects.all()
    serializer_class = PostDetailSerializer
# ≈ 6 sətir
```

> **Nəticə:** Generic views, eyni funksionallığı 4x az kodla verir.
> Real layihələrdə əsasən Generic istifadə olunur — lazım olduqda metodları override edirik.

---

# Swagger — API Sənədləməsi

`http://127.0.0.1:8000/api/docs/`

DRF-in Swagger inteqrasiyası (`drf_spectacular`) bütün endpointləri **avtomatik** sənədləndirir.
Heç bir əlavə kod yazmaq lazım deyil.

Swagger UI-da birbaşa:
- GET istəkləri göndərə bilərsiniz
- POST üçün form dolduraraq test edə bilərsiniz
- Hansı sahələrin məcburi olduğunu görürsünüz

---

# Yekun: Nə öyrəndik?

```
REST API     → JSON qaytaran API endpointi
Serializer   → Model ↔ JSON çevirmə + validation
@api_view    → Ən sadə DRF view (function)
APIView      → Sinif əsaslı, metodlar ayrı
Generic      → Hazır CRUD sinifləri — az kod, eyni nəticə
Swagger      → Avtomatik API sənədləməsi
```

---

# Ev Tapşırığı

## Tapşırıq: Comment Sistemi

### 1. Model (`blog/models.py`-a əlavə et)

### 2. APIView ilə Endpointlər

`APIView` istifadə edərək aşağıdakıları yaz:

| URL | Metod | Nə etməlidir |
|---|---|---|
| `/api/posts/<id>/comments/` | GET | Həmin postun bütün şərhlərini qaytar |
| `/api/posts/<id>/comments/` | POST | Həmin posta yeni şərh əlavə et |
| `/api/comments/<id>/` | DELETE | Şərhi sil |

### Əlavə olaraq

`PostDetailSerializer`-ə şərh sayını əlavə et:

`GET /api/posts/1/` cavabında bu sahə görünməlidir:
```json
{
  "id": 1,
  "title": "DRF dərsi",
  "comments_count": 3,
  ...
}
```
