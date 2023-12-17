<h1 align="center">ProductInventory</h1>

### ProductInventory, Python dilinde Flask kullanılarak geliştirilmiş bir stok kontrol uygulamasıdır. Bu uygulama, kullanıcıların ürünleri yönetmelerine, stok durumunu izlemelerine ve güncellemelerine olanak tanır.

<br>

## Proje'nin Özellikleri;

<br>

**Stok Takibi**: Her bir ürün için mevcut stok miktarını gösterir.

**Kullanıcı Dostu Arayüz**: Flask'ın esnekliğiyle oluşturulan kullanıcı dostu bir arayüz sunar. Bu arayüz, kullanıcıların kolayca gezinebilmesini ve istedikleri işlemleri hızlıca yapabilmelerini sağlar.

**Stok Güncellemesi**: Kullancılar ürünlerin stok miktarını kolaylıkla artırıp, azaltabilirler.

**Ürün Silme**: Bu özellik ile isteiğiniz ürünü silebilirsiniz.

**Detay Sayfası**: Ürünlerin detaylarını görmek için detay sayfasına gidebilirsiniz, bu sayfada şunlar;

-   Ürün Resmi
-   Ürün Adı
-   Ürünün Açıklaması
-   Stok Durumu
-   Stok Miktarı
-   Ürün düzenleme Butonu

bulunmaktadır.

### Proje de kullanılan modüller ve kütüphanler;

-   Flask
-   SqlAlchemy
-   Tailwind CSS

## Kurulum ve çalıştırma

<br>

**Projeyi klonlama**

```shell
git clone CLONE_URL
```

**Proje klasörne girin**

```shell
cd ProductInventory
```

**Gerekli bağımlılıkları yüklemek için**

```shell
pip install -r requirements.txt
```

**Projeyi çalıştırma**

-   Linux & Mac OS X

```shell
python3 main.py
```

-   Windows

```shell
python main.py
```

## Docker için Kurulum Adımları

**Projeyi klonlama**

```shell
git clone CLONE_URL
```

**Proje klasörne girin**

```shell
cd ProductInventory
```

**Docker image oluştuma**

```shell
 docker build -t python-app .
```

**Container'ı çalıştırma**

```shell
docker run -p 5000:5000 python-app
```

## Kullanım

**Normal kurulum için;**

Tarayıcınızın URL barına `http://127.0.0.1:5000` yazıp girmeniz yeterli.

<br>

**Docker kurulumu için;**

Tarayıcınızın URL barına `http://127.0.0.1:5000` veya `http://<local-ip-adresi>:5000` yazıp girmeniz yeterli.

### Proje ile ilgili bazı görseller

<br>

![products](/images/products_img.png)

<br>

![productadd](/images/productadd_img.png)

<br>

![products](/images/detail_img.png)

## Katkılar

Eğer projeye katkıda bulunmak isterseniz, lütfen bir Pull Requets oluşturun. Katkılarınızı bekliyoruz!

## Lisans

Bu proje [MIT lisansı](LICENSE) altında lisanslanmıştır.
