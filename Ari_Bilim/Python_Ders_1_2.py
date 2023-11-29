{
  "nbformat": 4,
  "nbformat_minor": 0,
  "metadata": {
    "colab": {
      "provenance": [],
      "include_colab_link": true
    },
    "kernelspec": {
      "name": "python3",
      "display_name": "Python 3"
    },
    "language_info": {
      "name": "python"
    }
  },
  "cells": [
    {
      "cell_type": "markdown",
      "metadata": {
        "id": "view-in-github",
        "colab_type": "text"
      },
      "source": [
        "<a href=\"https://colab.research.google.com/github/elanozturk/python/blob/main/Python_Ders_1_2.py\" target=\"_parent\"><img src=\"https://colab.research.google.com/assets/colab-badge.svg\" alt=\"Open In Colab\"/></a>"
      ]
    },
    {
      "cell_type": "code",
      "execution_count": null,
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "SkCvsmXx6fGx",
        "outputId": "9af35420-89be-4186-ed9b-bc7106709230"
      },
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "Merhaba Dünya\n"
          ]
        }
      ],
      "source": [
        "print(\"Merhaba Dünya\")"
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "print(\"36\")"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "24fLWFfT8FMF",
        "outputId": "5dda42e7-ec42-494a-baa9-9d0c833a79c1"
      },
      "execution_count": null,
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "36\n"
          ]
        }
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "uyari = \"Müşteri Hizmetlerine Başvurunuz\" #Değişken atama #String - str - Metinsel  # Müşreti uyarı metni"
      ],
      "metadata": {
        "id": "axYrXeDl8psk"
      },
      "execution_count": null,
      "outputs": []
    },
    {
      "cell_type": "code",
      "source": [
        "print(uyari)"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "3sKUceAz8_9d",
        "outputId": "6966df09-66b0-456f-e8ce-7764a32fcc21"
      },
      "execution_count": null,
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "Müşteri Hizmetlerine Başvurunuz\n"
          ]
        }
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "memleketim = \"Adana\""
      ],
      "metadata": {
        "id": "Y0aY35MmBoEi"
      },
      "execution_count": null,
      "outputs": []
    },
    {
      "cell_type": "code",
      "source": [
        "print(memleketim) #Yazdırma fonksiyonu"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "MSeBhCI_DKIF",
        "outputId": "56b2949b-ae4a-4cec-cd5b-dc05c98667d1"
      },
      "execution_count": null,
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "Adana\n"
          ]
        }
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "del(memleketim) #Silme fonksiyonu değişkeni hafızadan siler"
      ],
      "metadata": {
        "id": "1uopgXrN_wbe"
      },
      "execution_count": null,
      "outputs": []
    },
    {
      "cell_type": "code",
      "source": [
        "sayi = 1923 # integer - int - Tamsayı"
      ],
      "metadata": {
        "id": "PQTp3Xw4CSAf"
      },
      "execution_count": null,
      "outputs": []
    },
    {
      "cell_type": "code",
      "source": [
        "dolar = 28.64 # float - Ondalık Sayı"
      ],
      "metadata": {
        "id": "bnS8xst7B1nI"
      },
      "execution_count": null,
      "outputs": []
    },
    {
      "cell_type": "code",
      "source": [
        "type(sayi) #Veri tipi sorgulama fonksiyonu"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "Ag0NmIKFDwFx",
        "outputId": "3aa2fb2c-d3ee-408b-ff2e-badaa0f14f15"
      },
      "execution_count": null,
      "outputs": [
        {
          "output_type": "execute_result",
          "data": {
            "text/plain": [
              "int"
            ]
          },
          "metadata": {},
          "execution_count": 10
        }
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "type(dolar)"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "HA_bRDsEGqt3",
        "outputId": "1c0953b2-a741-4eac-a0ae-b45f2b16a677"
      },
      "execution_count": null,
      "outputs": [
        {
          "output_type": "execute_result",
          "data": {
            "text/plain": [
              "float"
            ]
          },
          "metadata": {},
          "execution_count": 11
        }
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "type(uyari)"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "nGRLjfGICdIP",
        "outputId": "af76b710-0b0e-45fa-9265-270cd8256ead"
      },
      "execution_count": null,
      "outputs": [
        {
          "output_type": "execute_result",
          "data": {
            "text/plain": [
              "str"
            ]
          },
          "metadata": {},
          "execution_count": 12
        }
      ]
    },
    {
      "cell_type": "markdown",
      "source": [
        "2.DERS"
      ],
      "metadata": {
        "id": "9i1qQAoaJtT-"
      }
    },
    {
      "cell_type": "code",
      "source": [
        "isim = \"Gökhan Kayan\""
      ],
      "metadata": {
        "id": "uzlUB4Gj6_fH"
      },
      "execution_count": null,
      "outputs": []
    },
    {
      "cell_type": "code",
      "source": [
        "print(isim)"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "NwmQsbUj7GDH",
        "outputId": "1ccc0613-f6bc-424c-a107-c971eda380e9"
      },
      "execution_count": null,
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "Gökhan\n"
          ]
        }
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "len(isim) #Karakter sayısınu bulma"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "8V3Zu5mB7uL4",
        "outputId": "89bebf0f-82de-413a-c4b5-24ee6b738c2b"
      },
      "execution_count": null,
      "outputs": [
        {
          "output_type": "execute_result",
          "data": {
            "text/plain": [
              "12"
            ]
          },
          "metadata": {},
          "execution_count": 11
        }
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "isim.lower() #tüm harfleri küçültme metodu"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/",
          "height": 35
        },
        "id": "XaGzW0GX85mq",
        "outputId": "12fcc2be-6d02-479d-f604-91c3cab4ed8c"
      },
      "execution_count": null,
      "outputs": [
        {
          "output_type": "execute_result",
          "data": {
            "text/plain": [
              "'gökhan kayan'"
            ],
            "application/vnd.google.colaboratory.intrinsic+json": {
              "type": "string"
            }
          },
          "metadata": {},
          "execution_count": 20
        }
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "isim.upper() #tüm harfleri büyütme metodu"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/",
          "height": 35
        },
        "id": "87cEl2ov9fSZ",
        "outputId": "bd7f0b0b-4057-4931-b881-57e087d6a2e8"
      },
      "execution_count": null,
      "outputs": [
        {
          "output_type": "execute_result",
          "data": {
            "text/plain": [
              "'GÖKHAN KAYAN'"
            ],
            "application/vnd.google.colaboratory.intrinsic+json": {
              "type": "string"
            }
          },
          "metadata": {},
          "execution_count": 13
        }
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "print(isim.title()) #Baş harfleri büyütme metodu"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "59EkifF09ziY",
        "outputId": "f18283d3-42a2-402a-e961-ec8ba3a98ce0"
      },
      "execution_count": null,
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "Gökhan Kayan\n"
          ]
        }
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "isim = int(input(\"İsmini Giriniz\"))"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "2ZLUzpRB-lUu",
        "outputId": "937cc7af-6261-470b-b41f-896895d04b15"
      },
      "execution_count": null,
      "outputs": [
        {
          "name": "stdout",
          "output_type": "stream",
          "text": [
            "İsmini Giriniz1923\n"
          ]
        }
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "print(isim)"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "ahNxfkU2AaCr",
        "outputId": "6a158d75-ee69-451b-d2c0-7ed4dc6e18bd"
      },
      "execution_count": null,
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "1923\n"
          ]
        }
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "type(isim)"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "me-tAmIyA-LA",
        "outputId": "9e42e373-a298-4c94-da7f-99ad8b6a456a"
      },
      "execution_count": null,
      "outputs": [
        {
          "output_type": "execute_result",
          "data": {
            "text/plain": [
              "str"
            ]
          },
          "metadata": {},
          "execution_count": 29
        }
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "isim = int(isim)"
      ],
      "metadata": {
        "id": "A8RJyXs6A1Ha"
      },
      "execution_count": null,
      "outputs": []
    },
    {
      "cell_type": "code",
      "source": [
        "type(isim)"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "ZhJIHDMyBJfY",
        "outputId": "f788394f-3415-4356-ad15-a57ea5445698"
      },
      "execution_count": null,
      "outputs": [
        {
          "output_type": "execute_result",
          "data": {
            "text/plain": [
              "int"
            ]
          },
          "metadata": {},
          "execution_count": 33
        }
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "cagri = \"20:00 İstanbul uçağımız kalkmaz üzeredir.\""
      ],
      "metadata": {
        "id": "qBzQ2nGzCZ29"
      },
      "execution_count": null,
      "outputs": []
    },
    {
      "cell_type": "code",
      "source": [
        "degisiklik = input(\"Yeni varış noktasını giriniz\")\n",
        "cagri = cagri.replace(\"İstanbul\",degisiklik)   #değişiklik metodu\n",
        "print(cagri)"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "sLM4SR8zCniu",
        "outputId": "4fa77f45-096d-44a6-c0e4-1d0234a8fd2a"
      },
      "execution_count": null,
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "Yeni varış noktasını girinizAfyon\n",
            "20:00 Malatya uçağımız kalkmaz üzeredir.\n"
          ]
        }
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "print(cagri)"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "8pza2rsADvEi",
        "outputId": "9dec3fd6-626e-42c6-ab8c-070db9138056"
      },
      "execution_count": null,
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "20:00 Malatya uçağımız kalkmaz üzeredir.\n"
          ]
        }
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "cagri.count(\"a\")"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "H6YHcCghJeag",
        "outputId": "b887dcc5-cc92-4491-b657-d8b276fe6387"
      },
      "execution_count": null,
      "outputs": [
        {
          "output_type": "execute_result",
          "data": {
            "text/plain": [
              "6"
            ]
          },
          "metadata": {},
          "execution_count": 54
        }
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "tekerleme = \"Bir berber bir berbere bre berber yeter\""
      ],
      "metadata": {
        "id": "W5VsUz2FKIU5"
      },
      "execution_count": null,
      "outputs": []
    },
    {
      "cell_type": "code",
      "source": [
        "buyuk = tekerleme.upper()\n",
        "print(buyuk)\n",
        "buyuk.count(\"BIR\")"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "s6V8rd96KOW1",
        "outputId": "882e7704-4a6a-4dc2-a344-90b4adbf88f9"
      },
      "execution_count": null,
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "BIR BERBER BIR BERBERE BRE BERBER YETER\n"
          ]
        },
        {
          "output_type": "execute_result",
          "data": {
            "text/plain": [
              "0"
            ]
          },
          "metadata": {},
          "execution_count": 72
        }
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "isim = \"Damla\"\n",
        "soyisim =\"Şenbabaoğlu\""
      ],
      "metadata": {
        "id": "vxTqtCrBMczB"
      },
      "execution_count": null,
      "outputs": []
    },
    {
      "cell_type": "code",
      "source": [
        "isim + \" \" + soyisim"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/",
          "height": 35
        },
        "id": "lF78C9n9MksK",
        "outputId": "09bbfe27-fc6d-47cc-ef5b-9b39e218ba98"
      },
      "execution_count": null,
      "outputs": [
        {
          "output_type": "execute_result",
          "data": {
            "text/plain": [
              "'Damla Şenbabaoğlu'"
            ],
            "application/vnd.google.colaboratory.intrinsic+json": {
              "type": "string"
            }
          },
          "metadata": {},
          "execution_count": 116
        }
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "sayi = 1923"
      ],
      "metadata": {
        "id": "Qsr4xsk_NOYV"
      },
      "execution_count": null,
      "outputs": []
    },
    {
      "cell_type": "code",
      "source": [
        "isim =\"Hakan\""
      ],
      "metadata": {
        "id": "m8Zs8glTNr8V"
      },
      "execution_count": null,
      "outputs": []
    },
    {
      "cell_type": "code",
      "source": [
        "adres = \"Ankara\""
      ],
      "metadata": {
        "id": "gIfwGzdLNuI0"
      },
      "execution_count": null,
      "outputs": []
    },
    {
      "cell_type": "code",
      "source": [
        "isim = adres\n",
        "print(isim)"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "jxGXfoebNryt",
        "outputId": "2e975e99-a271-40f9-8a8c-2dcee8468065"
      },
      "execution_count": null,
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "Ankara\n"
          ]
        }
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "isim = 1923.15\n",
        "type(isim)"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "ZXCi7BqFNeb9",
        "outputId": "78f49a93-d828-4224-9160-6a53edff2d45"
      },
      "execution_count": null,
      "outputs": [
        {
          "output_type": "execute_result",
          "data": {
            "text/plain": [
              "float"
            ]
          },
          "metadata": {},
          "execution_count": 96
        }
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "isim = \"Doğa\"\n",
        "soyisim = \"Gül\"\n",
        "print(isim + \" \" +soyisim)"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "2_8N_vhQNRbt",
        "outputId": "0ffd3f86-eb0f-4f94-8e02-fc1f3cb8bb46"
      },
      "execution_count": null,
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "Doğa Gül\n"
          ]
        }
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "isim[-4:-1]"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/",
          "height": 35
        },
        "id": "zXcY1LjgPqjo",
        "outputId": "8a98749d-157b-4233-8b0e-00279858d817"
      },
      "execution_count": null,
      "outputs": [
        {
          "output_type": "execute_result",
          "data": {
            "text/plain": [
              "'Doğ'"
            ],
            "application/vnd.google.colaboratory.intrinsic+json": {
              "type": "string"
            }
          },
          "metadata": {},
          "execution_count": 138
        }
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "isim = input(\"İsim Giriniz\")\n",
        "soyisim = input(\"Soyisim Giriniz\")\n",
        "sirketadresi = \"aribilgi.com\"\n",
        "\n",
        "mail = isim+\".\"+soyisim+\"@\"+sirketadresi\n",
        "mail = mail.lower()\n",
        "mail = mail.replace(\"ş\",\"s\")\n",
        "mail = mail.replace(\"ü\",\"u\")\n",
        "mail = mail.replace(\"ö\",\"o\")\n",
        "mail = mail.replace(\"ç\",\"c\")\n",
        "mail = mail.replace(\"ı\",\"i\")\n",
        "mail = mail.replace(\"ğ\",\"g\")\n",
        "print(mail)\n",
        "\n",
        "# mail adresi oluştur\n",
        "# bütün harfler küçük\n",
        "# türkçe karakterle olmayacak\n",
        "# sukru.tercan@aribilgi.com\n"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "miJWy_KKRvs7",
        "outputId": "55df1576-d49d-461b-91e5-de89d878b4b2"
      },
      "execution_count": null,
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "İsim GirinizDoğa\n",
            "Soyisim GirinizGül\n",
            "doga.gul@aribilgi.com\n"
          ]
        }
      ]
    }
  ]
}