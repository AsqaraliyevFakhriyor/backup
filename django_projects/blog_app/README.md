# Simple `BLOG SITE๐` in python๐ `django` firemwork!


### [!] project maded with [mohirev.uz](https://www.mohirdev.uz) tutorials!

>[INFO] Blog web site which you can read news posted by admin, its 
> has `authorization๐` modul so users can signup admin can 
> *post, delete, edit* news and `controls` users at the same time




## Dependeces ๐
1. python-3.9.2+


### Cloning from GitHub

```bash
    git clone https://github.com/AsqaraliyevFakhriyor/blogsite_webapp <PRIOJECT_DIR>
    cd <PROJECT_DIR>
```

### Pip **requerements** ๐ฆ

1. django==3.1.*




### Installing ๐ ๏ธ
1. Creating virtual enviroment with `venv`

```bash
    python -m venv vevn
    source venv/Script/activate
```
! if you are `Mac` or `Linux` users you can use the code belove to activate `VENV`:
```bash
    source vevn/bin/activate
```

2. Installing pip requirements
>[!] Installing requirements.txt ๐
```bash
    pip install -r requirements.txt
```
> ! You must change `pip` to `pip3` if you are **Mac** or **Linux** user


3. Seting **DATABASE**๐ django uses !`sqlite3`๐๏ธ
```bash
    touch 'db.sqlite3'
    python manage.py makemigrations
    python manage.py migrate
```
> ! You must change `python` to `python3` if you are **Mac** or **Linux** user

### Runing application ๐

```bash
    python manage.py runserver
```

# DISCLAIMER โโโ
> ! This project maded for only learning purposes!, there maybe drowbacks, bugs or even security problems!
> I am (Asqaraliyev Faxriyor) is not responsible for any issues with `project`
