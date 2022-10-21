{
  "cells": [
    {
      "cell_type": "markdown",
      "metadata": {
        "id": "view-in-github",
        "colab_type": "text"
      },
      "source": [
        "<a href=\"https://colab.research.google.com/github/david716150308/ddd/blob/master/line.py\" target=\"_parent\"><img src=\"https://colab.research.google.com/assets/colab-badge.svg\" alt=\"Open In Colab\"/></a>"
      ]
    },
    {
      "cell_type": "code",
      "execution_count": 15,
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "QI4p6mpJJJpo",
        "outputId": "045c97ef-45c4-40d1-cf7c-71fdc1b648bf"
      },
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "Looking in indexes: https://pypi.org/simple, https://us-python.pkg.dev/colab-wheels/public/simple/\n",
            "Requirement already satisfied: line-bot-sdk in /usr/local/lib/python3.7/dist-packages (2.3.0)\n",
            "Requirement already satisfied: flask in /usr/local/lib/python3.7/dist-packages (1.1.4)\n",
            "Requirement already satisfied: flask-ngrok in /usr/local/lib/python3.7/dist-packages (0.0.25)\n",
            "Requirement already satisfied: requests>=2.0 in /usr/local/lib/python3.7/dist-packages (from line-bot-sdk) (2.23.0)\n",
            "Requirement already satisfied: future in /usr/local/lib/python3.7/dist-packages (from line-bot-sdk) (0.16.0)\n",
            "Requirement already satisfied: aiohttp>=3.7.4 in /usr/local/lib/python3.7/dist-packages (from line-bot-sdk) (3.8.3)\n",
            "Requirement already satisfied: asynctest==0.13.0 in /usr/local/lib/python3.7/dist-packages (from aiohttp>=3.7.4->line-bot-sdk) (0.13.0)\n",
            "Requirement already satisfied: async-timeout<5.0,>=4.0.0a3 in /usr/local/lib/python3.7/dist-packages (from aiohttp>=3.7.4->line-bot-sdk) (4.0.2)\n",
            "Requirement already satisfied: frozenlist>=1.1.1 in /usr/local/lib/python3.7/dist-packages (from aiohttp>=3.7.4->line-bot-sdk) (1.3.1)\n",
            "Requirement already satisfied: typing-extensions>=3.7.4 in /usr/local/lib/python3.7/dist-packages (from aiohttp>=3.7.4->line-bot-sdk) (4.1.1)\n",
            "Requirement already satisfied: yarl<2.0,>=1.0 in /usr/local/lib/python3.7/dist-packages (from aiohttp>=3.7.4->line-bot-sdk) (1.8.1)\n",
            "Requirement already satisfied: charset-normalizer<3.0,>=2.0 in /usr/local/lib/python3.7/dist-packages (from aiohttp>=3.7.4->line-bot-sdk) (2.1.1)\n",
            "Requirement already satisfied: aiosignal>=1.1.2 in /usr/local/lib/python3.7/dist-packages (from aiohttp>=3.7.4->line-bot-sdk) (1.2.0)\n",
            "Requirement already satisfied: attrs>=17.3.0 in /usr/local/lib/python3.7/dist-packages (from aiohttp>=3.7.4->line-bot-sdk) (22.1.0)\n",
            "Requirement already satisfied: multidict<7.0,>=4.5 in /usr/local/lib/python3.7/dist-packages (from aiohttp>=3.7.4->line-bot-sdk) (6.0.2)\n",
            "Requirement already satisfied: idna<3,>=2.5 in /usr/local/lib/python3.7/dist-packages (from requests>=2.0->line-bot-sdk) (2.10)\n",
            "Requirement already satisfied: chardet<4,>=3.0.2 in /usr/local/lib/python3.7/dist-packages (from requests>=2.0->line-bot-sdk) (3.0.4)\n",
            "Requirement already satisfied: certifi>=2017.4.17 in /usr/local/lib/python3.7/dist-packages (from requests>=2.0->line-bot-sdk) (2022.9.24)\n",
            "Requirement already satisfied: urllib3!=1.25.0,!=1.25.1,<1.26,>=1.21.1 in /usr/local/lib/python3.7/dist-packages (from requests>=2.0->line-bot-sdk) (1.24.3)\n",
            "Requirement already satisfied: itsdangerous<2.0,>=0.24 in /usr/local/lib/python3.7/dist-packages (from flask) (1.1.0)\n",
            "Requirement already satisfied: click<8.0,>=5.1 in /usr/local/lib/python3.7/dist-packages (from flask) (7.1.2)\n",
            "Requirement already satisfied: Werkzeug<2.0,>=0.15 in /usr/local/lib/python3.7/dist-packages (from flask) (1.0.1)\n",
            "Requirement already satisfied: Jinja2<3.0,>=2.10.1 in /usr/local/lib/python3.7/dist-packages (from flask) (2.11.3)\n",
            "Requirement already satisfied: MarkupSafe>=0.23 in /usr/local/lib/python3.7/dist-packages (from Jinja2<3.0,>=2.10.1->flask) (2.0.1)\n"
          ]
        }
      ],
      "source": [
        "!pip install line-bot-sdk flask flask-ngrok"
      ]
    },
    {
      "cell_type": "code",
      "execution_count": 16,
      "metadata": {
        "id": "pmvkY6DQDu5z"
      },
      "outputs": [],
      "source": [
        "from flask_ngrok import run_with_ngrok\n",
        "from flask import Flask, request\n",
        "import json\n",
        "\n",
        "app = Flask(__name__)\n",
        "\n",
        "@app.route(\"/\", methods=['POST'])\n",
        "def linebot():\n",
        "    body = request.get_data(as_text=True)\n",
        "    json_data = json.loads(body)\n",
        "    print(json_data)               # 印出 json_data\n",
        "    return 'OK'"
      ]
    },
    {
      "cell_type": "code",
      "execution_count": 17,
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/",
          "height": 36
        },
        "id": "ylkDvkEfEZIw",
        "outputId": "aff42f8f-2d71-4357-981f-4b1ba0da61c6"
      },
      "outputs": [
        {
          "output_type": "execute_result",
          "data": {
            "text/plain": [
              "'\\n掛載Google硬碟\\n安裝套件\\n引用套件\\nAPP應用準備\\n消息準備\\nhandler執行方法設計\\n啟動應用\\n\\n'"
            ],
            "application/vnd.google.colaboratory.intrinsic+json": {
              "type": "string"
            }
          },
          "metadata": {},
          "execution_count": 17
        }
      ],
      "source": [
        "'''\n",
        "掛載Google硬碟\n",
        "安裝套件\n",
        "引用套件\n",
        "APP應用準備\n",
        "消息準備\n",
        "handler執行方法設計\n",
        "啟動應用\n",
        "\n",
        "'''"
      ]
    },
    {
      "cell_type": "code",
      "execution_count": 18,
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "2mDqhB78Fxp6",
        "outputId": "ea3a3c61-e941-4be2-da60-661d054e9486"
      },
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "Drive already mounted at /content/drive; to attempt to forcibly remount, call drive.mount(\"/content/drive\", force_remount=True).\n"
          ]
        }
      ],
      "source": [
        "'''\n",
        "\n",
        "資料 mapping 至google drive\n",
        "\n",
        "把資料寫在/content/drive\n",
        "\n",
        "即可保存在 google drive內\n",
        "\n",
        "'''\n",
        "from google.colab import drive\n",
        "drive.mount('/content/drive')"
      ]
    },
    {
      "cell_type": "code",
      "execution_count": 19,
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/",
          "height": 36
        },
        "id": "4iGRs1oYD6Ca",
        "outputId": "c06ac855-4cc3-49fe-fa86-d652193812e1"
      },
      "outputs": [
        {
          "output_type": "execute_result",
          "data": {
            "text/plain": [
              "'\\n\\n流程解析\\n\\n'"
            ],
            "application/vnd.google.colaboratory.intrinsic+json": {
              "type": "string"
            }
          },
          "metadata": {},
          "execution_count": 19
        }
      ],
      "source": [
        "'''\n",
        "\n",
        "流程解析\n",
        "\n",
        "'''\n"
      ]
    },
    {
      "cell_type": "code",
      "execution_count": 20,
      "metadata": {
        "id": "rJDNE2TYEaYA"
      },
      "outputs": [],
      "source": [
        "'''\n",
        "引用套件\n",
        "'''\n",
        "\n",
        "# 引用Web Server套件\n",
        "from flask import Flask, request, abort, jsonify\n",
        "\n",
        "# 載入json處理套件\n",
        "import json\n",
        "\n",
        "# 外部連結自動生成套件\n",
        "from flask_ngrok import run_with_ngrok\n",
        "\n",
        "# 從linebot 套件包裡引用 LineBotApi 與 WebhookHandler 類別\n",
        "from linebot import (\n",
        "    LineBotApi, WebhookHandler\n",
        ")\n",
        "\n",
        "# 引用無效簽章錯誤\n",
        "from linebot.exceptions import (\n",
        "    InvalidSignatureError\n",
        ")\n",
        "import requests\n",
        "import urllib.request\n",
        "import json\n",
        "import time\n",
        "from flask_ngrok import run_with_ngrok\n",
        "from flask import Flask, request\n",
        "\n",
        "# 載入 LINE Message API 相關函式庫\n",
        "from linebot import LineBotApi, WebhookHandler\n",
        "from linebot.exceptions import InvalidSignatureError\n",
        "from linebot.models import MessageEvent, TextMessage, TextSendMessage,LocationMessage\n",
        "\n",
        "# 載入 json 標準函式庫，處理回傳的資料格式\n",
        "import json\n",
        "import  urllib.request,csv\n",
        "import requests\n",
        "import urllib.request\n",
        "import json\n",
        "import time\n",
        "import math\n"
      ]
    },
    {
      "cell_type": "code",
      "execution_count": 21,
      "metadata": {
        "id": "XssY97Y9Eahe"
      },
      "outputs": [],
      "source": [
        "'''\n",
        "建置主程序\n",
        "\n",
        "建置handler與 line_bot_api\n",
        "'''\n",
        "\n",
        "# 設定Server啟用細節\n",
        "app = Flask(__name__,static_url_path = \"/material\" , static_folder = \"./material/\")\n",
        "run_with_ngrok(app)\n",
        "\n",
        "# 生成實體物件\n",
        "line_bot_api = LineBotApi(\"ubCrXTe09xLd2r413RELz309xMh7VRioIFvXQjSGY8VXZBMwj/9ehWnO7GnvZoPXDuDSGLwaWHLAA0etSvOMhR7woyCvKQime2MjodExBuvvl5M+6DHRm9X/wwrAvXvN4fZXJKa/KAAdIYh+G6O7kQdB04t89/1O/w1cDnyilFU=\")\n",
        "\n",
        "#收發消息專用\n",
        "handler = WebhookHandler(\"d4d4ff4c7e592ee87125f500dd0fae89\")"
      ]
    },
    {
      "cell_type": "code",
      "execution_count": 22,
      "metadata": {
        "id": "jyIFMBi4EvTl"
      },
      "outputs": [],
      "source": [
        "'''\n",
        "建置主程序的API入口\n",
        "  接受Line傳過來的消息\n",
        "  並取出消息內容\n",
        "  將消息內容存在google drive的檔案內\n",
        "  並請handler 進行消息驗證與轉發\n",
        "'''\n",
        "\n",
        "# 啟動server對外接口，使Line能丟消息進來\n",
        "@app.route(\"/\", methods=['POST'])\n",
        "def callback():\n",
        "    # get X-Line-Signature header value\n",
        "    signature = request.headers['X-Line-Signature']\n",
        "\n",
        "    # get request body as text\n",
        "    body = request.get_data(as_text=True)\n",
        "    print(body)\n",
        "    #print(body['source'][\"userId\"])\n",
        "    #line_bot_api.get_profile('<user_id>')\n",
        "\n",
        "    # 記錄用戶log\n",
        "    f = open(\"/content/drive/MyDrive/ai-event.log\", \"a\")\n",
        "    f.write(body)\n",
        "    f.close()\n",
        "\n",
        "    # handle webhook body\n",
        "    try:\n",
        "        handler.handle(body, signature)\n",
        "    except InvalidSignatureError:\n",
        "        abort(400)\n",
        "\n",
        "    return 'OK'"
      ]
    },
    {
      "cell_type": "code",
      "execution_count": 23,
      "metadata": {
        "id": "kpVdUJ0wTSli"
      },
      "outputs": [],
      "source": [
        "'''\n",
        "Button篇\n",
        "    設定模板消息，指定其參數細節。\n",
        "\n",
        "'''\n",
        "\n",
        "\n",
        "#引入所需要的消息與模板消息\n",
        "from linebot.models import (\n",
        "    MessageEvent, TemplateSendMessage , PostbackEvent\n",
        ")\n",
        "\n",
        "#引入按鍵模板\n",
        "from linebot.models.template import(\n",
        "    ButtonsTemplate\n",
        ")\n",
        "\n",
        "\n",
        "'''\n",
        "alt_text: Line簡覽視窗所出現的說明文字\n",
        "template: 所使用的模板\n",
        "ButtonsTemplate: 按鍵模板\n",
        "    thumbnail_image_url: 展示圖片\n",
        "    title: 標題\n",
        "    text: 說明文字\n",
        "    actions: 模板行為所使用的行為\n",
        "    data: 觸發postback後用戶回傳值，可以對其做商業邏輯處理\n",
        "\n",
        "'''\n",
        "#其他teemplateSendMessage\n",
        "#Python Line-bot-sdk ConfirmTimplate\n",
        "#alt_text :初步的檢視文字(預覽)\n",
        "#title是標題\n",
        "#text是文字描述\n",
        "#actions:按鈕，就是json\n",
        "#案件範本最多只能有四個json的部分\n",
        "buttons_template_message = TemplateSendMessage(\n",
        "    alt_text='Buttons template',\n",
        "    template=ButtonsTemplate(\n",
        "        title='歡迎使用午餐小幫手',\n",
        "        text='請點擊下方按鈕來尋找今日的午餐吧',\n",
        "        actions=[\n",
        "          {\n",
        "            \"type\": \"uri\",\n",
        "            \"label\": \"找餐廳\",\n",
        "            \"uri\":\"https://line.me/R/nv/location/\",\n",
        "            \"data\": \"Data1\"\n",
        "\n",
        "          },\n",
        "          \n",
        "          \n",
        "        ],\n",
        "  )\n",
        ")"
      ]
    },
    {
      "cell_type": "code",
      "execution_count": 24,
      "metadata": {
        "id": "CsDjhbugRh9Z"
      },
      "outputs": [],
      "source": [
        "'''\n",
        "\n",
        "設計一個字典\n",
        "    當用戶輸入相應文字消息時，系統會從此挑揀消息\n",
        "\n",
        "'''\n",
        "\n",
        "# 將消息模型，文字收取消息與文字寄發消息 引入\n",
        "from linebot.models import (\n",
        "    MessageEvent, TextMessage, TextSendMessage, ImageSendMessage,LocationMessage\n",
        ")\n",
        "\n",
        "# 根據自定義菜單四張故事線的圖，設定相對應image\n",
        "template_message_dict = {\n",
        "  \"@more\":buttons_template_message,\n",
        "}"
      ]
    },
    {
      "cell_type": "code",
      "execution_count": 25,
      "metadata": {
        "id": "gUFnh86kQSzk"
      },
      "outputs": [],
      "source": [
        "# 用戶發出文字消息時， 按條件內容, 回傳文字消息\n",
        "@handler.add(MessageEvent, message=TextMessage)\n",
        "def handle_message(event):\n",
        "    #event.message.text 用戶傳來的文字內容\n",
        "    #若有find 特殊符號@就執行下面的程序，從字典裡找答案\n",
        "    #若無 回應查無此字\n",
        "    if(event.message.text.find('@')!= -1):\n",
        "        line_bot_api.reply_message(\n",
        "        event.reply_token,\n",
        "        template_message_dict.get(event.message.text)\n",
        "        )\n",
        "    else:\n",
        "        line_bot_api.reply_message(\n",
        "        event.reply_token,\n",
        "        TextSendMessage(text=\"歡迎使用午餐小幫手~，請輸入@more來找你今天的餐廳吧\")\n",
        "        )\n",
        "@handler.add(MessageEvent, message=LocationMessage)\n",
        "def linebotres(event):\n",
        "    body = request.get_data(as_text=True)\n",
        "    json_data = json.loads(body)\n",
        "    list2=[]\n",
        "    #print(json_data[\"events\"][0][\"message\"][\"latitude\"])               # 印出 json_data\n",
        "    #print(json_data)\n",
        "    x=event.message.latitude\n",
        "    y=event.message.longitude\n",
        "    z=event.message.address\n",
        "    list1=[]\n",
        "    print(z)\n",
        "    restaurant(z,event.source.user_id)\n",
        "    list1.clear ()\n",
        "    list2.clear ()\n"
      ]
    },
    {
      "cell_type": "code",
      "execution_count": 28,
      "metadata": {
        "id": "yB_tWG1FPOzx"
      },
      "outputs": [],
      "source": [
        "list1=[]\n",
        "list2=[]\n",
        "def get_latitude_longtitude(address):#地址轉換經緯度\n",
        "    # decode url\n",
        "    address = urllib.request.quote(address)\n",
        "    GOOGLE_API_KEY = 'AIzaSyCzi7Oo5zdMVZuDq1Txu1k-gUfHuAi5zNI'\n",
        "    url = \"https://maps.googleapis.com/maps/api/geocode/json?address=\" + address + '&key=' + GOOGLE_API_KEY\n",
        "    while True:\n",
        "        res = requests.get(url)\n",
        "        js = json.loads(res.text)\n",
        "\n",
        "        if js[\"status\"] != \"OVER_QUERY_LIMIT\":\n",
        "            time.sleep(1)\n",
        "            break\n",
        "\n",
        "    result = js[\"results\"][0][\"geometry\"][\"location\"]\n",
        "    lat = result[\"lat\"]\n",
        "    lng = result[\"lng\"]\n",
        "    list1.append(lat)\n",
        "    list1.append(lng)\n",
        "    #print(lat,lng)\n",
        "    #print(list1)\n",
        "    return lat, lng\n",
        "\n",
        "def getDistance(latA, lonA, latB, lonB):#計算距離\n",
        "    ra = 6378140  # 赤道半徑\n",
        "    rb = 6356755  # 極半徑\n",
        "    flatten = (ra - rb) / ra  # Partial rate of the earth\n",
        "    # change angle to radians\n",
        "    radLatA = math.radians(latA)\n",
        "    radLonA = math.radians(lonA)\n",
        "    radLatB = math.radians(latB)\n",
        "    radLonB = math.radians(lonB)\n",
        "\n",
        "    pA = math.atan(rb / ra * math.tan(radLatA))\n",
        "    pB = math.atan(rb / ra * math.tan(radLatB))\n",
        "    x = math.acos(math.sin(pA) * math.sin(pB) + math.cos(pA) * math.cos(pB) * math.cos(radLonA - radLonB))\n",
        "    c1 = (math.sin(x) - x) * (math.sin(pA) + math.sin(pB)) ** 2 / math.cos(x / 2) ** 2\n",
        "    c2 = (math.sin(x) + x) * (math.sin(pA) - math.sin(pB)) ** 2 / math.sin(x / 2) ** 2\n",
        "    dr = flatten / 8 * (c1 - c2)\n",
        "    distance = ra * (x + dr)\n",
        "    distance = round(distance / 1000, 4)\n",
        "    #print(distance)\n",
        "    return distance\n",
        "from linebot.models import MessageAction, TemplateSendMessage, ConfirmTemplate\n",
        "from linebot import LineBotApi, WebhookHandler\n",
        "# 需要額外載入對應的函示庫\n",
        "from linebot.models import MessageAction, TemplateSendMessage, CarouselTemplate,  CarouselColumn\n",
        "from linebot import LineBotApi, WebhookHandler\n",
        "# 需要額外載入對應的函示庫\n",
        "from linebot.models import PostbackAction,URIAction, MessageAction, TemplateSendMessage, ButtonsTemplate,LocationSendMessage\n",
        "import random\n",
        "\n",
        "\n",
        "def restaurant(address,name):#爬取餐廳\n",
        "    url = ' https://gis.taiwan.net.tw/XMLReleaseALL_public/Restaurant_C_f.csv'\n",
        "    webpage = urllib.request.urlopen(url)  #開啟網頁\n",
        "    data = csv.reader(webpage.read().decode('utf-8').splitlines()) #讀取資料到data陣列中\n",
        "    get_latitude_longtitude(address)\n",
        "    for i in data:\n",
        "         if i !=[]:\n",
        "            #print(\"aaa\")\n",
        "            if i[16]!=None and i[17]!=None:\n",
        "                if i[16]!='Px' and i[17]!=\"Px\":\n",
        "                    if getDistance(list1[0],list1[1],float(i[17]),float(i[16]))<10:\n",
        "                      list2.append(i[1])#店名\n",
        "                      list2.append(i[2])#介紹\n",
        "                      list2.append(i[3])#地址\n",
        "                      list2.append(i[16])#\n",
        "                      list2.append(i[17])#\n",
        "                      list2.append(getDistance(list1[0],list1[1],float(i[17]),float(i[16])))\n",
        "    \n",
        "    import random\n",
        "    if list2==[]:\n",
        "      line_bot_api.push_message(name,TextSendMessage(text=\"很抱歉你附近沒有餐廳喔\"))\n",
        "      print(list2)          \n",
        "    elif len(list2)<=30 and len(list2)>0:\n",
        "      print(list2)\n",
        "      line_bot_api.push_message(name,TextSendMessage(text=\"恭喜你抽到了\"))\n",
        "      for i in range(0,len(list2),6):\n",
        "        print(list2[i])\n",
        "        line_bot_api.push_message(name,TextSendMessage(text=str(list2[i])))\n",
        "        line_bot_api.push_message(name,TextSendMessage(text=list2[i+1]))\n",
        "        line_bot_api.push_message(name,LocationSendMessage(\n",
        "            title=str(list2[i]),\n",
        "            address=\"地址:\"+list2[i+2],\n",
        "            latitude=list2[i+4],\n",
        "            longitude=list2[i+3]\n",
        "        )\n",
        "      )\n",
        "      list1.clear ()\n",
        "      list2.clear ()\n",
        "\n",
        "    else:\n",
        "      line_bot_api.push_message(name,TextSendMessage(text=\"恭喜你抽到了\")) \n",
        "      print(list2)\n",
        "      for i in range(5):\n",
        "        x = random.randrange(0, len(list2), 6)\n",
        "        #print(list2[x])\n",
        "      #line_bot_api.push_message(name,TextSendMessage(text=\"恭喜你抽到了\"))\n",
        "      #for i in range(x,x+30,6):\n",
        "        #print(list2[i])\n",
        "        line_bot_api.push_message(name,TextSendMessage(text=str(list2[x])))\n",
        "        line_bot_api.push_message(name,TextSendMessage(text=list2[x+1]))\n",
        "        line_bot_api.push_message(name,LocationSendMessage(\n",
        "            title=str(list2[x]),\n",
        "            address=\"地址:\"+list2[x+2],\n",
        "            latitude=list2[x+4],\n",
        "            longitude=list2[x+3]\n",
        "        )\n",
        "      )\n",
        "      list1.clear ()\n",
        "      list2.clear ()\n",
        "      #line_bot_api.push_message(name,TextSendMessage(text=list2[i+1]))\n",
        "      "
      ]
    },
    {
      "cell_type": "code",
      "execution_count": null,
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "NVkYb65fHY9W",
        "outputId": "aa2c3938-8f52-40cb-8718-d0275adc267c"
      },
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            " * Serving Flask app \"__main__\" (lazy loading)\n",
            " * Environment: production\n",
            "\u001b[31m   WARNING: This is a development server. Do not use it in a production deployment.\u001b[0m\n",
            "\u001b[2m   Use a production WSGI server instead.\u001b[0m\n",
            " * Debug mode: off\n"
          ]
        },
        {
          "output_type": "stream",
          "name": "stderr",
          "text": [
            "INFO:werkzeug: * Running on http://127.0.0.1:5000/ (Press CTRL+C to quit)\n"
          ]
        },
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            " * Running on http://93d8-34-86-109-38.ngrok.io\n",
            " * Traffic stats available on http://127.0.0.1:4040\n",
            "{\"destination\":\"U6de184dd73098dc6aac0c20771365461\",\"events\":[{\"type\":\"message\",\"message\":{\"type\":\"location\",\"id\":\"16987918405568\",\"latitude\":23.10483,\"longitude\":121.274412,\"address\":\"983台灣花蓮縣富里鄉東富公路\"},\"webhookEventId\":\"01GFWDKEFNPH3MS54RDGZJE33F\",\"deliveryContext\":{\"isRedelivery\":false},\"timestamp\":1666327361697,\"source\":{\"type\":\"user\",\"userId\":\"Ubb57a8e3858e81e2227bf969196bd849\"},\"replyToken\":\"d7eb9103defa4bdbbeaa494d03ce2bd6\",\"mode\":\"active\"}]}\n",
            "983台灣花蓮縣富里鄉東富公路\n",
            "['東河休閒農場', '民國79年政府創導休閒農業，經農委會同意東河成立休閒農業區，並由農委會委請嘉義農專負責規劃。農場首先就舊有七、八莊舍及分場部員工宿舍整建為民宿，闢建樟樹林步道，民國80年開始營運。起初來訪遊客與本場員工共用餐廳，體驗榮民生活，該七、八莊舍至今仍在東河遊憩區內，欲體驗榮民早期生活者不妨來此參觀。至86年觀光局納入輔導補助，整建餐廳、渡假小屋(現為別墅區)等設施，農場設備漸臻完善。於87年改善通訊設備、路燈照明設施，延建樟樹林步道(即現之生態步道)，新建涼亭、花架等休閒設施，使遊憩區設施完備。民國89年拆除共育室改裝之和室新建桃莊，90年整建獨棟之桃莊庭院提供遊客更好的住宿設備，並整建兒童遊戲區供兒童遊玩。至今，東河休閒農場仍與周圍榮民眷屬維持良好關係，時而可見附近榮民至本場販賣現採水果，鮮嫩多汁，吮指回味。東河休閒農場本身則配合政府政策，致力於農業轉型無毒有機農業，配合觀...', '臺東縣959東河鄉北源村67號', '121.300360', '23.074740', 7.0392, '玉蟾園', '玉蟾園是一家座落於臺東池上鄉錦園村，八公頃自然生態園，充滿生活藝術，非常漂亮的名宿，提供好喝的咖啡及極具特色的客家風味餐；可以預約團體ＤＩＹ活動。', '臺東縣958池上鄉錦園村新開園162號', '121.226740', '23.112540', 5.9828, '秋菊皂坊', '取自天然、用於天然、還之天然 在池上定居二十年的手工皂達人陳秋菊，從思考校園營養午餐廢油回收再利用開始，關注生態環保的議題。「讓自己生活的社區更環保、更健康、更適合下一代居住」，秉持這樣的信念，她一頭栽進創作手工皂的領域。秋菊自費研習並投入大量心力，從化腐朽為神奇的環保皂、到沙拉脫、洗衣粉等日常清潔用品，她一邊製作手工皂，一邊想著如何連結發展在地特色，將花東縱谷蘊藏的豐沛物產、及各式各樣精華融進色澤樸實的手工皂中，並適切地針對不同肌膚個性來調配用皂、沐浴乳配方，研發創意親子同樂的藝術琉璃皂和保養品教學 / DIY / 手工皂師資培訓等等。 除了沐浴洗顏皆適宜使用的手工皂產品之外，能夠讓客人們發揮創意、享受動手趣味的幸福串皂─ 使用天然的材料，以嚴謹的態度執行每道工序，製作出一塊塊獨一無二的手工皂，而皂上的特製文字鋼印，也蘊含著別出心裁的祝福與問候。串皂外型可愛討喜，掛置...', '臺東縣958池上鄉仁愛路191號', '121.219730', '23.122500', 6.3037, '臺東縣池上鄉農會', '店內招牌「紫米餅」獲選為2012臺東縣十大旅遊伴手禮暨特色美食。本產品係以臺東縣池上鄉農會輔導契作生產之稻米為主要原料，經過碾製而成的米粒與池上鄉農會輔導生產的黑糯米相接合，再給與膨發之後，作成紫米餅。本會紫米餅與市面上的米膨發製品米果或仙貝等有所差異區隔，市售米製品大多以甜食為主，且色澤為白色或褐色，特推出「紫米餅」吸引消費者的注意，也為米餅市場提供新的選擇。【資料來源：池上網路商城】', '臺東縣958池上鄉中山路302號', '121.219370', '23.124910', 6.285, '池上鄉農會-展售中心', '池上鄉農會是全台唯一結合精緻碾米加工與稻米教育之觀光工廠，廠區旁有池上花海美景，廠區內設有展售中心，金色豐收館內含文化區及田媽媽美食坊，還可預約爆米香DIY體驗及豐收飯。', '臺東縣958池上鄉新興村7鄰85-6號', '121.202790', '23.112260', 8.2811]\n",
            "東河休閒農場\n",
            "玉蟾園\n",
            "秋菊皂坊\n",
            "臺東縣池上鄉農會\n",
            "池上鄉農會-展售中心\n"
          ]
        },
        {
          "output_type": "stream",
          "name": "stderr",
          "text": [
            "INFO:werkzeug:127.0.0.1 - - [21/Oct/2022 04:42:51] \"\u001b[37mPOST / HTTP/1.1\u001b[0m\" 200 -\n"
          ]
        },
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "{\"destination\":\"U6de184dd73098dc6aac0c20771365461\",\"events\":[{\"type\":\"message\",\"message\":{\"type\":\"location\",\"id\":\"16987920632442\",\"latitude\":24.158966,\"longitude\":120.670832,\"address\":\"404台灣台中市北區健行路827號\"},\"webhookEventId\":\"01GFWDMCW6CXQGN8F6S0GBWP2H\",\"deliveryContext\":{\"isRedelivery\":false},\"timestamp\":1666327392768,\"source\":{\"type\":\"user\",\"userId\":\"Ubb57a8e3858e81e2227bf969196bd849\"},\"replyToken\":\"e076f115df954c9b94dc9cf69550205b\",\"mode\":\"active\"}]}\n",
            "404台灣台中市北區健行路827號\n",
            "['PAPAMIA義式廚房', '創立於1995年的帕帕咪雅，有一位充滿理想與堅持的女老闆，老闆顏小姐表示，當初她就讀大學時讀的是觀光系，當時便對義大利美食嚮往不已，畢業後不但開了一家義大利餐廳，更花了半年時間到義大利學習正統義大利料理，十多年來仍常常利用時間赴義大利學習進修，可以說是將所有的精神與時間都投注在義大利美食的烹調料理。老闆表示，帕帕咪雅不以裝潢取勝，強調餐點的品質。對於餐點的烹調風格，則是80%保有義大利正統口味，而20%則經過口味調整，而最有趣的，就是這裡的sauce與麵是分開點的，有7種麵與20種sauce可以組合！', '臺中市407西屯區東興路三段412-1號', '120.655840', '24.158490', 1.5243, '春水堂-大墩店', '精明一街，人稱台中第一街，它是造街運動的傳奇，是外國旅人拜訪台中必經之地。而整條精明一街的人氣，幾乎通通都在春水堂大墩店這裡凝聚。露天紅色傘海下的坐位，滿滿都是享受悠閒的人們，愜意寫在臉上，輕鬆掛在笑裡，點杯珍奶或翡翠檸檬就這樣坐一下午。 大墩店自1987年開張，2008年重新整修，全新的空間設計表現當代的東方美學，幽雅沈靜，明式線條原木桌椅、灰磚牆、別緻燈籠 字畫、陶器相融其間…。並設置秋山堂精品茶庄， 角落玄關的花藝造景古色古香，處處驚喜。大墩店的室外，呈現出歐式浪漫。室內，卻 是一派中式儒雅，木桌椅、紅磚牆、燈籠字畫交 址陶….古色古香，角落玄關的花藝造景，處處驚喜。吸煙區：一樓外廣場\\u3000\\u3000禁煙區：室內全禁煙', '臺中市403西區大墩十九街9號', '120.655850', '24.156150', 1.5537, '南瓜屋義式餐飲', '一間餐廳要能在台中存活超過五年可不是件簡單的事，而老餐廳能大手筆投資讓自己改頭換面成為另一番風貌就更不簡單了。1997年開幕的南瓜屋位在國立台灣美術館對面那條多采多姿，充滿著餐廳茶坊的街上，是間小有名氣的特色餐廳，然而南瓜屋並不以此自滿，在大幅改裝後最近又重新開幕了。', '臺中市403西區五權西四街108號', '120.662450', '24.135920', 2.6888, '鄉村鵝廚房美式餐廳', '鄉村鵝廚房位在清幽的存中街上，洋溢著美式鄉村風格。庭院中聳立著三棵老樹～玉蘭花及杉木。夏天時玉蘭花盛開，院子與室內清香瀰漫讓人陶醉。陽光穿越葉隙撒落一片光彩，花兒綻放吐露清香，庭院內小橋流水多麼詩情畫意。店主人過去是知名餐廳「茹蕬葵」的廚師，處理牛排擁有過人水準；老闆娘過去是「長榮桂冠」的調酒師，擁有一間店是兩人共同的夢想，鄉村鵝則是圓夢的結晶，料理上紮實的真本事連外國人都讚不絕口，還有超級大公關拉不拉多犬Bonnie可愛又溫馴，鄉村鵝是您不可錯過的優質餐廳。', '臺中市403西區存中街19號', '120.660740', '24.141090', 2.2278, '聖華宮素菜餐廳-大雅店', '台中大雅店成立84年7月，以歐式自助餐為主題，95年11月已重新規劃裝潢，並以「現點現吃、吃到飽」之嶄新型態呈現，舒適的用餐環境，廣受顧客好評。本著創造建康、分享顧客，精挑細選出天然的食材，不斷研究、創新，來體現蔬食養生亦能兼顧精緻、味美，以滿足每一位顧客的需求。', '臺中市404北區大雅路555號', '120.671720', '24.171430', 1.3857, '黃記鵝肉', '鮮黃色的招牌，在街口中閃耀著，您會很容易發現這裡，因為從傍晚營業開始，一直到深夜，湧進的顧客人潮不斷，精選的鵝肉，搭配醬料，肉質鮮美、多汁，美味讓人意猶未盡。', '臺中市400中區大誠街43號', '120.678730', '24.145270', 1.7143, '赤鬼炙燒牛排-崇德店', '台中赤鬼牛排餐廳為日船美食連鎖系統之子公司，日船美食連鎖系統包含了：日船章魚小丸子、日船重口味麵線、台中赤鬼牛排餐廳；日船美食連鎖系統自1995年起投入餐飲研究領域，我們堅持以【立足台灣、放眼國際】的事業經營理念，將美食文化推及世界各地，在這期間，正因為堅持，日船美食連鎖系統的事業版圖已跨足：美加地區、港澳地區、中國大陸地區、東南亞地區。', '臺中市406北屯區文心路四段603號', '120.685220', '24.172410', 2.0886, '炭火燒肉工房', '走進「炭火燒肉工房」，會有種讓人放鬆的感覺。喝碗灑上蔥花的雞湯，點杯清酒小酌，三五好友隨聊，還沒開始用餐，就已是享受。進門便能感受到十足活力，炭火燒肉工房充滿著年輕氣息，包括店長以下都屬年輕族群，使得店內氣氛熱鬧活潑，沒有絲毫疏離感。當炭火將上等食材烤得滋滋作響，傳來的香味，是種誘惑。一口吃下，你將會明白，真正的美味，不需過於複雜的烹調或醃漬。歡迎來到「炭火燒肉工房」，品嚐簡單卻會令人感動的絕妙滋味！', '臺中市403西區美村路一段412號', '120.661590', '24.143620', 1.94, '烤狀猿日式炭火燒肉-一中店', '烤狀猿 保有最傳統的炭火燒烤，煙燻的特殊風味是一般無煙燒肉無法比擬的，讓客人吃到最新鮮、最美味是我們的堅持，不論是何種食材，皆是一時之選，手工處理的肉類食材，口感有別一般機器處裡，本店的特殊沾醬更是讓您回味無窮。', '臺中市404北區太平路8-1號', '120.686110', '24.147650', 1.9941, '泰炘泰式料理', '泰炘泰式料理以重酸重辣的泰國菜，在附近眾多異國料理店家中獨樹一格，多年來口碑始終屹立不搖、深受肯定。簡單、家常卻道道經典的菜單，在泰國主廚的用心烹調下，有著令人難忘的美味功力。「泰炘」以展現泰菜酸辣精神著稱，但若您要求調整口味，貼心親切的店家主人也樂於為您特別製作。如果飯後想來一杯清涼飲料，不妨試試泰式傳統涼茶，不同於台灣飲料，泰式傳統涼茶顏色是胡蘿蔔色，是泰國特有的紅茶粉加上煉乳調製而成，喝起來香濃可口，十分順口。', '臺中市403西區公正路242-1號', '120.658620', '24.149110', 1.6513, '台中金典酒店 歐廷地中海料理', '全國唯一，於單一餐廳裡同時由不同的主廚現場烹調美食料理，不必搭飛機出國就可以享受到各國美食疑次滿足您對異國料理的喜好。提供各國風味的午晚餐，各式珍饈海鮮、義大利麵及精緻甜點享用不盡，讓人流連忘返，意猶未盡，道道精選，值得品嚐。彷彿悠遊在海鮮美食的變幻繽紛中。美麗而優雅的裝潢，讓您如置身貴族般的享受。喜愛獨特料理的朋友一定要來品嚐。', '臺中市403西區健行路1049號', '120.663170', '24.155970', 0.8455, '新天地餐飲集團-崇德旗艦店', '新天地崇德旗艦店，擁有氣派華麗的宴會廳與中式料理餐廳；1樓「樂食自助百匯」提供上百道中西式美饌、飲品、甜點等，以及現點現做料理，鮮美滋味饕客最愛；餐廳內設置兒童遊戲區，亦是親子餐廳首選；另外，數個獨立包廂大宴小酌廣受家族聚會與商務人士青睞！除了一般用餐之外，新天地崇德旗艦店擁有專業的婚禮企畫團隊，提供新人籌畫婚禮服務，並有時尚華麗的婚宴場地、典雅證婚儀式堂，是中部地區首屈一指的婚宴場地。', '臺中市406北屯區崇德五路345號（崇德路與崇德五路口）', '120.684140', '24.179120', 2.6119, '京華煙雲', '京華煙雲是以林語堂大師名著為名的主題餐廳，有著室內設計專長的老闆羅友竹小姐，特將餐廳風格定位在三、四零年代，中國北方大宅院印象，建造前，還特別到北京取經，擷取詩人、政商名流故居特色，讓京華煙雲每個角落充滿京城文人的風雅氣息！是台中少數以文學原創作品大方呈現的餐飲空間。不論是「京華煙雲」四字，對聯、餐墊、壁畫，到大小高低錯落有緻的書畫燈飾，皆出自聞名中部的藝術家庭～柯耀東及夫人郭皆貴老師之手；而門口紅包車更是許多來美術園道拍攝婚紗、留影的景點首選。', '臺中市403西區五權七街57號', '120.663210', '24.135060', 2.7567, '八分飽', '成立於1994年，以川菜和上海菜為主的『八分飽』餐廳，迄今已走過十多個年頭。老闆和老闆娘從年輕時即投入餐飲業，秉持「飯吃八分飽、做事十分勤」原則，對於品質與口味十分堅持，也獲得許多顧客支持。', '臺中市403西區模範街9巷37號', '120.665460', '24.147840', 1.3458, '新天地餐飲集團-東區店', '新天地東區店座落台中市東區旱溪東邊，景色優美，鄰近74號快速道路交通便利。歐風建築佔地寬廣，成為台中市民宴客場地首選，採用先進的LED屏及尖端科技影音設備，搭配高雅的色系呈現皇室氣息，彰顯出新人的貴族氣勢；專業的「婚禮企劃團隊」提供完善及多元化與婚禮專業相關服務，是新人最嚮往的夢幻結婚場地．數個大小宴會廳、包廂，更是大型活動、團體餐會的最佳場地，多元功能一應俱全，讓活動更精彩！另外，館內還有西洋博物館、瀚熙軒中式餐廳，是親子出遊、朋友約會的好去處！', '臺中市401東區旱溪東路一段456號', '120.701460', '24.141980', 3.6361, '春天素食餐廳', '春天素食餐廳秉持初衷，「捍衛健康，預防勝於治療的理念」由平常的飲食著重於體內環保，自然的養生觀念，讓人們將傳統素食的印象改觀。', '臺中市407西屯區大墩十七街88號2樓', '120.648160', '24.155750', 2.331, '春水堂-豐樂店', '春水堂豐樂店於2000年元月正式成立，設店在台中南屯區的湖水岸藝術街內，緊臨豐樂雕塑公 園，四周欖仁樹環繞，在台中這個急速發展中的城市，對於想要遠離都市紛擾與忙碌的人來說，湖 水岸藝術街是一個悠閒的角落，有許多風格獨具的戶外休閒座，白天黑夜都各自有其迷人的氛圍。豐樂店有三個樓層，100個廣場座位，一二樓提供一般茶飲及餐點的消費，三樓是古典悠雅的小 壺泡空間，豐樂店臨近幅員遼闊的公園，周圍更有許多精品店，是相當適合全家大小凝聚感情和三 五好友聯誼的好地方。吸煙區：一樓戶外廣場、三樓外陽台\\u3000\\u3000禁煙區：室內全禁煙', '臺中市408南屯區文心南五路321號之13號', '120.644590', '24.131950', 4.0067, '瑪露連嫩仙草總店', '滑嫩的仙草搭配Q香芋圓，再淋上奶油球，直接入口，多達10種的嫩仙草，香氣逼人。另外這裡也是三種冰的創始店，紅豆、Q芋、珍珠等冰品，充分展現其獨特美味!', '臺中市400中區臺灣大道一段255號', '120.662440', '24.149890', 1.3166, '幸發亭蜜豆冰 - 健行店', '陳冠溢先生繼承了幸發亭創始人的精神，注重品質、真材實料，給予客人最好的服務。懷古情懷的空間象徵著幸發亭時代傳承的經典，除了古早味的蜜豆冰外，店中也有不少獨特的產品帶給客人無限驚喜！', '臺中市404北區健行路465號', '120.678470', '24.159000', 0.7763, '東東芋圓', '頗具地方小吃特色的東東芋圓，非常適合做國民旅遊的推動景點，遊客若來大坑踏青、爬山，可來此嘗嘗芋圓的美味，而且一年四季，全年無休夏季以冰品為主，強調Q度口感，冬季以熱湯為主，加入紅豆湯、桂圓湯、薑汁或是燒仙草，別具一番風味，在寒冷的冬天裡來上一碗，可趨寒並提振精神。採用美國進口濾水器，水質保証乾淨、甘甜、衛生，讓客人享用的安心。', '臺中市406北屯區東山路二段48-3號', '120.741070', '24.179810', 7.5023, '蘭莊法式蔬食咖啡館', '主人是煮咖啡、品嚐咖啡的高手，料理則是用進口有機蔬菜配上獨自研發調製的sauce醬的美味養生蔬食。在大坑的山邊溪旁，享受健康美食，也享受自然。咖啡與蔬食複合料理館「蘭莊」位在風景宜人的大坑山區，是個空地遼闊、三面景緻宜人、紫蘭花盆景環立屋外的浪漫西餐廳。 而「蘭莊」取自店主夫妻名中各自的最後一字，莊園以健康食材為料理方向，幫助忙碌的現代人，補充營養，並為都市人有一個很好的聚會場所。', '臺中市406北屯區東山路二段51-35號', '120.741790', '24.180770', 7.6051, '春水堂-四維店', '位於台中女中後方，市政府、地方法院及眾多學校的鄰居，看似祥和的文教區，其實十多年前激起驚天駭浪，處在冷飲文化的發跡地，見證了革命與歷史。身處暴風眼中，雖然漣漪已擴散，但是產生風暴的翅膀卻從未停歇過。超過四分之一世紀以來，堅持與美麗的屹立著。有人一喝就是數十年，有人一喝就是從小到大，多少人在這見證了友情、愛情、親情，少女漸漸變成少婦。無數杯的珍奶，在這裡端出；無數個故事，在這裡上演；無數次的情感交流，在這裡產生。也許青春不再，但是風華依舊，這裡就是春水堂的創始店；台中市西區四維店。吸煙區：一樓\\u3000\\u3000禁煙區：地下樓', '臺中市403西區四維街30號', '120.675740', '24.137710', 2.4044, '咕嚕咕嚕原住民音樂餐廳', '咕嚕咕嚕音樂餐廳．原住民文化會館座落在美術館前綠園道上。外觀以漂流木做設計，傳達自然與人文合一的訊息。您可以品嚐到原住民傳統料理與創意餐點的結合，食材來自台東金鋒鄉新興部落耕種的新鮮野菜及蔬果，部分美食是從新興部落宅急便運送到餐廳限量供應。\\u3000\\u3000邱老闆本身是排灣族原住民，您可以在用餐時分聽見他唱著一首首部落之歌，在歌聲中彷彿可以看到陽光、海洋或是豐收的田野，大自然與靈魂美好的共鳴。咕嚕咕嚕的logo是一群攜手相連的人，象徵著族群的融合，願能將此美好訊息傳遞出去。並且用最原味的食材,烹飪出最具原味風格的饗宴,咕嚕,咕嚕特有的節奏與旋律,咀嚼原住民濃厚的人文氣息,原住民的老闆,海而海先生,將他的原住民本領完全充分的發揮在這個音樂園地,原住民的飲食文化,原住民的建築美學,原住民的拿手歌喉以及原住民的幽默風趣,完完全全的展現在咕嚕咕嚕音樂餐廳', '臺中市403西區五權西四街13巷2號', '120.662500', '24.139030', 2.3628, '竹之鄉風味餐廳', '竹之鄉於72年在大坑圓環開幕營業素來是以竹筒飯為招牌料理，而廣受青睞其主要宗旨就是充滿竹料理之雅致的美味氣氛。竹之鄉精心篩選成熟之孟宗竹作為取材，用蒸汽濃縮之科技將竹本身蘊含數種天然胺機酸，濃縮至竹料理內。', '臺中市406北屯區東山路二246-1', '120.739450', '24.178560', 7.3036, '谷明土雞城', '來到大坑，想要嚐嚐竹筍大餐與全雞三吃的饗宴，這裡是一個好選擇，標榜純田園風味的『谷明』土雞城，充滿著鄉間農村的氣息，菜色也是料好實在，正統的土雞、筍仔雞湯，還有特製的醃酸梅也別具一格、滋味獨特。', '臺中市406北屯區大坑里光西巷227號', '120.753450', '24.202250', 9.6685, '安可喬治龍蝦螃蟹美式海鮮餐廳', '安可喬治提供快速又親切的服務，你絕不可錯過他提供的美味大餐。例如，北大西洋龍蝦、阿拉斯加大肉蟹、或是每隔十天從緬因州、阿拉斯加與新斯科細亞省進口的海產，真正愛好海鮮的人一定不可錯過這個地方。食材頂級、味道鮮美。吃過讓人懷念再三！平均每人消費都在2000元以上！建議您先打電話預約，不然可能需要等候一段時間喔！ (周日公休)', '臺中市408南屯區大業路492號', '120.639470', '24.153890', 3.236, '春水堂-中科永福店', '每一家春水堂都各具生命力和文化氣質、卻能傳遞相同的核心價值。中科永福店用Villa的觀點營造一個茶館空間，挑高的視覺，一牆流水瀑、一株白千層、幾張鴉片床和以椰殼設計的桌子都不落痕跡地帶給人們一種自在與放鬆。當你走進春水堂中科永福店中，悅耳的音樂、舒適的環境與滿溢的幸福香氣，讓你可以在這裡悠閒、安心地品嚐手中的好茶好心情。中科永福店位於台中市西屯區永福路，中科進駐後，帶動沿線發展，加上鄰近東海大學、藝術街等特色景點，讓永福路成為中科地區生活機能的主要區段。吸煙區：一樓室外\\u3000\\u3000禁煙區：室內全禁煙', '臺中市407西屯區永福路141號', '120.621010', '24.185080', 5.8317, '艾凡里咖啡美食', '艾凡里於1994年在藝術街坊誕生，至今已過了13年，一如清秀佳人安妮的經典故事，在歲月流逝中沈澱發酵，成為人們心裡嚮往的美夢。服務人員的親切笑容，典雅溫馨的空間氛圍，精緻專業的豐富美食…似乎每個角落都美好的可以寫下一首詩篇。原來，不用遠赴愛德華王子島，就能讓美夢實現。透過艾凡里十多年來累積的點點滴滴，店主人在咖啡專業領域裡更往下栽根，延伸出的咖啡地圖，探討咖啡豆、器具、煮咖啡等各個層面，讓咖啡更貼近生活，也讓艾凡里的咖啡喝起更有一股濃醇深厚的底韻。', '臺中市434龍井區藝術街33號', '120.594300', '24.187660', 8.4019, '狀元仙草舖-東興店', '無', '臺中市408南屯區東興路二段350號', '120.653230', '24.144700', 2.3853, '幸發亭蜜豆冰 - 北平店', '民國27年,最早的蜜豆冰(ミツマメ)是龍井區人 陳溪先生在台中火車站旁,以手推車沿街叫賣的方式經營的,當時的蜜豆冰是參考日本的四果冰,再加上十多種配料製成的.民國32年左右,進入第一市場,終於有個小小的攤位,並將攤位命名為[辛發亭].在一次大火中, 辛發亭幸運的只有招牌和少部分店面受損,於是火災後[辛發亭]便改名為[幸發亭],希望能夠化辛酸為幸運.豐富配料的蜜豆冰是當年許多學生、阿兵哥、台中人記憶中的好味道，近幾年來也陸續開發新產品,例如雪綿冰、手工豆花、嫩仙草等.數十年來秉持實在用心的經營理念，目前已交由第三代經營，繼續傳承這令人懷念的美妙滋味.推薦菜單：招牌蜜豆冰、紅豆牛奶冰、芒果冰、各類雪綿冰', '臺中市404北區北平路2段98-2號', '120.675190', '24.171440', 1.453, '泰妃苑泰式料理', '位在台中西屯路三段的異國料理路段，泰妃苑代表泰式料理在此坐鎮；一般泰式料理給人的觀念是，很酸、很辣、很重口味，根深蒂固在台灣人的腦海中，但在泰妃苑，主廚在泰式料理界打滾十多餘年，知道饕客要的是什麼，並想在泰式料理上做些改變，一直有別於一般想法的他，決定自身出來開店，要實現自己的夢想，並帶給喜愛泰式料理的饕客一個全新的體驗。。', '臺中市407西屯區西屯路三段166號之46號', '120.655800', '24.164260', 1.637, '碧綠素食餐飲有機園', '台中素食‧碧綠健康園以『希望地球健康，人類健康的宗旨』而開設，最早因親人得癌症過世，受姜淑惠醫師的錄音帶所啟發，也受李秋涼老師精神感召，得知很多疾病均由於平日食物攝取過多的油脂、毒素所造成，所以將原本葷食生意改成現在碧綠健康園有十年的時間。', '臺中市407西屯區中工三路184號', '120.617880', '24.176740', 5.7304, '素樂活廚房', '素樂活廚坊提供最精緻的美味素食，為台中素食餐廳的新典範。想一嚐不一樣的台中素食美食嗎？素樂活廚坊是您最佳的選擇！台中素食餐廳中的翹楚，將素食化身為不一樣的西式料理，顛覆傳統素食的刻板印象，誰說素食不能有更好、更新的選擇！', '臺中市407西屯區漢口路二段121號', '120.661140', '24.165030', 1.1933, '寬心園-文心公益店', '寬心園是一家結合了中國禪風以及日本美學，並透過現代極簡設計來呈現的精緻蔬食館。菜餚的部分強調美味與創意，結合傳統台菜、法義烹調與港日料理的精髓，創造出無國界的蔬食新風貌。嚴選優質蔬菜、菇菌、穀麥與水果食材，運用低鹽、少油的自然烹調方法，製作出一系列天然與健康的蔬食新料理。', '臺中市408南屯區文心路一段435號(公益路上近文心路口)', '120.646500', '24.150660', 2.6376, '禾野酵素生活館', '禾本股份有限公司(GRAIN-ROOT CORP),創辦人為董事長陳清裕藥師,總公司成立於民國八十三年。陳董事長為專業的藥師，認為中國人是吃米的民族，而日本則早就有將酵素添加在米飯之內改善白飯品質之做法，所以”禾本股份有限公司”成立之初期以銷售”炊飯素”為主，而”稻米”在生物分類上屬於”禾本科”這也是”禾本股份有限公司”命名的由來。民國九十四年四月，第一家\\u3000禾野酵素生活館於此開幕。', '臺中市407西屯區四川路18號', '120.687140', '24.171770', 2.1827, '赤鬼炙燒牛排-台灣大道店', '台中赤鬼牛排餐廳為日船美食連鎖系統之子公司，日船美食連鎖系統包含了：日船章魚小丸子、日船重口味麵線、台中赤鬼牛排餐廳；日船美食連鎖系統自1995年起投入餐飲研究領域，我們堅持以【立足台灣、放眼國際】的事業經營理念，將美食文化推及世界各地，在這期間，正因為堅持，日船美食連鎖系統的事業版圖已跨足：美加地區、港澳地區、中國大陸地區、東南亞地區。 遙想數十年前”牛排館”是平價好吃與高品質專業排餐的代名詞，但，如今遍觀市場上大多是採複合式沙拉吧經營的牛排餐廳，食材豐富多樣卻也忽略了許多愛吃排餐，但對於沙拉吧卻意願低落的消費者，一間真正專業牛排餐廳應有的樣子與原始初衷似乎被消費者漸漸遺忘 為此，赤鬼牛排餐廳因而成立，我們的經營目標就是要滿足這些愛吃排餐的消費者，我們沒有豐富的沙拉吧，也沒有精緻的服務，我們只有專業的五塊肉，我們回歸到牛排餐廳都應有的最原始初衷，專注於提供最高品質的肉...', '臺中市403西區臺灣大道二段170號', '120.670230', '24.150850', 0.8988, '中非咖啡', '中非咖啡是台中市知名老咖啡館。老闆咖啡達人廖仁村先生三十多年咖啡烘培的經驗，把咖啡豆當成畫布，獨家研發的烘培和咖啡調製法，讓咖啡成為值得回味的藝術品，歡迎喜愛咖啡的人來品嚐。', '臺中市403西區四維街46號', '120.674780', '24.138520', 2.2977, '2派克脆皮雞排-東海直營店', '本店提供寬敞的空間，液晶電視，以及無線上網服務，讓你在舒適的環境，享受鮮嫩可口、香甜多汁的2派克脆皮雞排，另提供多樣的點心產品。', '臺中市434龍井區新興路76號', '120.586130', '24.181680', 8.9679, '春水堂-國際店', '國際店位於台中市東海藝術商圈，坐在店內其實能感受十分悠閒的氣氛，尤其在傍晚時分，來到這個地方，就是要放鬆自己的心情，享受一下喝茶的樂趣，這裡的夜晚就較白天來的浪漫許多，藝術街上人來人往散步著，能感受到在這充滿著涼爽的氣息。吸煙區：一樓 外廣場\\u3000\\u3000禁煙區：室內全禁煙', '臺中市434龍井區藝術街48號', '120.593940', '24.187780', 8.4408, '2派克脆皮雞排-台中黎明店', '超級獨家配方醃製，將雞肉炸得外脆內嫩，厚實肉質裡飽含鮮甜湯汁，搭配酥、香、脆的外皮，愈嚼愈香甜，讓味蕾無限滿足。', '臺中市408南屯區永定里黎明路2段56號', '120.637400', '24.144100', 3.7747, '印月創意東方宴', '台中美食餐廳-印月-創意東方宴從食材的本質思考；用創意為五感提味，以燈光點燃空間情境；將藝術融入時尚文化。得意料理人做菜以理想為出發點，每一道菜從料理到擺盤，看似純淨、其實豐富，都是挑動食慾與滿足視覺的經典創作。讓食的時間以享受為單位，慢慢流動、緩緩嚐味！(本文選自印月創意東方宴 官網)', '臺中市408南屯區公益路二段818號', '120.628510', '24.151640', 4.3765, '富鼎旺豬腳', '位在台中中華路夜市旁邊的『富鼎旺極品豬腳餐廳』，總是飄來陣陣香味，讓許多經過的民眾都忍不著聞香而來，每逢用餐時間，都得排隊等上一會兒，才有可口豬腳美食可以享用！ 老師傅每天早上7點就得開始準備魯豬腳，經過篩選、洗淨、整理等過程，再依循古法細燉慢熬3至4小時，火候掌控得宜，才能呈現豬腳的精華。', '臺中市400中區臺灣大道一段560號', '120.676550', '24.145280', 1.6214, '臺中金典酒店', '臺中金典酒店，座落於臺中交通樞紐、最繁華的商業地段，不論您來自何方，請讓我們以最貼心的服務，帶領您進入臺中這個富含創意及文化魅力的都市！', '臺中市403西區健行路1049號', '120.663170', '24.155970', 0.8455, '潭子臭豆腐', '取名潭子臭豆腐，是因為老闆的上一代真的是從潭子推車到台中來賣臭豆腐的。這裡的臭豆腐和向上路的梁婆婆臭豆腐口感不大一樣，口味各有千秋，梁婆婆的豆腐內外炸得更為酥脆，而潭子臭豆腐的內部則比較保留軟綿多汁的口感，醬汁的蒜味也比較不那麼重，個人覺得是臭豆腐界中比較清爽耐吃的口味。', '臺中市400中區中華路與民族路交叉口', '120.676360', '24.144660', 1.6791, '四十年老店雞蛋蚵仔煎', '位於全家便利商店旁的40年老店雞蛋蚵仔煎是到中華路必吃的。除了蚵仔煎是必點外，其他還有豬肝湯、麻油腰子、炒三鮮等，因為食材很新鮮，所以味道當然一級棒。這裡的蚵仔煎蚵仔鮮美，粉皮煎得微微焦脆，加上空心菜菜莖脆脆的口感，以及甜鹹適中的醬料，真是給他100分。麻油腰子的鮮度也是沒話說，雕花的腰子和清爽不膩的麻油，以及提味的老薑片，一吃完心裡就覺得有補到。炒三鮮加了醋提味，吃起來感覺很開胃。', '臺中市400中區中華路一段197號', '120.677590', '24.146240', 1.566, '50年代台北蚵仔麵線', '大大的蚵仔，就是「50年代台北老牌蚵仔麵線」的最佳代言人，肥茲茲又新鮮的蚵仔讓消費者讚不絕口，也奠定了在台中中華夜市的閃亮名聲！ 中華路夜市內的40年小吃店，創始人簡金萬先生原是台北艋舺人，在偶然的機緣下，邀請台中朋友品嚐台北的蚵仔麵線，並來到台中經營蚵仔麵線小吃店，深獲台中朋友的喜愛，一轉眼就經過了40年的光陰。招牌蚵仔麵線選用嘉義布袋的飽滿鮮蚵，以及有十足嚼勁的大腸一同享用，鮮度與甜味十足，加上台灣道地的手工麵線，完整呈現台灣小吃的精華之處。目前提供超過50道料理，滿足每一位饕客的胃。', '臺中市400中區中華路一段199號', '120.677530', '24.146280', 1.5594, '正老牌麵線糊', '正老牌麵線糊頂著這老招牌闖蕩忠孝夜市三四十年，從小路邊攤到現今的店面，老闆用心經營是大家有目共睹的。每次看到所勺子上的麵線糊真的是料多實在，而且每碗的麵線糊幾乎是要滿出來，最後淋在麵線上的醬汁是老闆的獨門醬料，美味且道地的麵線糊就在眼前了!!麵線糊有三種配料可選，有肉羹麵線、蚵仔麵線、魷魚嘴麵線，每種都是40元，任選兩種口味的話是50元，如果想要吃到3種口味那就要點綜合麵線而且只要60元!!趕快來嚐嚐忠孝老招牌美食正老牌麵線糊!!', '臺中市402南區合作街 70-2號', '120.681390', '24.129660', 3.4166, '一中豐仁冰', '賣冰一世人\\u3000鹹酸甜都嚐     一碗冰，賣了超過一甲子時光，養活一家三代數十口人。老闆娘說，一中豐仁冰是很多人共同的回憶，特別是台中一中、體育大學的學生，他們總是一下課就來吃冰，畢業後，有機會回到一中街也會過來吃碗冰，感覺相當親切。一中豐仁冰裡面，有香濃滑口的牛奶冰淇淋、酸梅冰沙及蜜紅豆，嚐起來甜甜、酸酸又鹹鹹，正謂「鹹酸甜」的冰品，令人百吃不膩。', '臺中市404北區育才街3巷4號之6', '120.686650', '24.149000', 1.9489, '昇和甘草芭樂', '位於一中街上的「昇和甘草芭樂」，專賣現切的新鮮水果，從挑選、洗淨到切塊，每一個步驟都不馬虎，水果的品質佳、份量多、價格實在，讓學生、上班族都非常信賴。老闆曾在傳統市場經營30多年的水果攤，對於水果的挑選嚴格且專業，希望讓顧客吃的安心、吃的健康。', '臺中市404北區一中街', '120.685380', '24.150300', 1.7616, '一家之薯', '美國進口的馬鈴薯，高溫烤熟後將馬鈴薯切開，淋上獨家醬汁，排上預備好的新鮮食材，撒上起司粉，即可拿在手香濃起司，忍不住想要咬下熱呼呼的起司...眾多食材蝦仁、杏鮑菇、鳳梨、章魚、燻雞肉等....店家推薦：切達起司、青花菜起司、玉米起司、鮮蝦起司。', '臺中市407西屯區文華路永新巷南二弄58號', '120.645550', '24.176810', 3.2427, '一心素食臭豆腐', '「一心素食臭豆腐」在逢甲夜市熱賣十多年，獨家好口味不僅受到茹素者歡迎，就連葷食者也讚不絕口。老闆黃先生與太太兩人固守品質與口碑，堅持選用當日新鮮現做的豆腐，要控制好豆腐發酵的程度，炸起來才會金黃酥脆、爽口不油膩。老闆說，臭豆腐要好吃，必須掌控時間與油溫，過與不及都會影響口感，每一個動作都要紮實做好，不能因為客人催促而破壞品質，有時候寧可讓客人排隊等候，也不願為了衝量而失去原有的水準。細心、貼心，成就一心臭豆腐今日的景色。', '臺中市407西屯區福星路461巷2號 (歐跑運動用品店旁)', '120.645440', '24.177960', 3.3306, '阿蒝師中東沙威瑪', '超人氣『阿蒝師沙威瑪』，開店至今以超過15年之久。以道地、傳統的中東口味受到歡迎，一整串層層疊起的雞肉，用慢火旋轉方式烘烤，散發出濃郁香氣，吸引顧客們聞香而來。配料超豐富．大口吃過癮，老闆王先生和太太為顧及品質，堅持只用新鮮食材，當日現做的柔軟麵包夾入烤得入味的雞肉、高麗菜、起司、小黃瓜，並搭配沙拉、番茄醬、胡椒，口感多層次、口味獨特！份量足夠，大口大口吃最過癮！', '臺中市404北區精武路316號', '120.684050', '24.146520', 1.9233, '京悅港式飲茶', '經營港式飲茶超過二十年的王老闆，多年來，堅持保留流動餐車送上點心的特色，現耗資千萬，在臺中友百貨12樓，開設他心目中時尚、高雅的港式飲茶餐廳，以單純的黑與白，搭配進口百盞燈具，營造絕美餐廳風格，溫暖又不失特色，讓舊雨新知一吃滿意。', '臺中市404北區三民路三段179號A棟12樓', '120.681880', '24.147580', 1.6869, '半月燒餡餅專賣店-一中總店', '盧的堡半月燒．一中總店\\u3000「半月燒」三個字一直在初次遇見的人心中存在著問號，這個似中非中、東瀛味頗重的名稱，常讓一中街夜市的人潮不免好奇駐足觀賞。排隊美食推薦．鐵板現炒半月燒\\u3000據盧老闆詮釋，「半月」代表的是獨家配方由手工現場製作的麵皮，現炸的滋味，酥中帶Q，不油不膩，而「燒」便是現場不斷傳出高溫鐵板燒熱炒的聲音，有別於蔥油餅、抓餅、烙餅的製作方法，而突破傳統的創新餅類美食，再加上店家堅持品質、熱情服務，正是半月燒極欲賦予饕客們心中幸福的記號。一中街排隊美食\\u3000人氣小吃\\u3000熱情的人潮簇擁，見證了半月燒的美味；除了美味外，半月燒更堅持在如此繁忙的一中夜市裡「品質不走調、服務不折扣」，一定要用最細膩的精神回饋顧客的愛護。～新鮮食材．現點現做．平價美味．天天超人氣～', '臺中市404北區育才南街31號（一中二街商圈，水利大樓旁）', '120.686180', '24.147990', 1.9763, '梨子咖啡館-崇德店', '想讓你嘗到美夢成真的滋味。跨過小橋走入莊園，推開木造大門—繪本室裡的嘻笑聲，在樓中樓木窗櫺間搖曳；特製的綠意沙發旁，家人正與幸福櫥窗共餐。從樓梯往下望，右邊是隱密的日式餐區；往上走，梨葉蔓生整片天花板，望見西式餐區，以及海灣木屋戶外餐區的驚喜！親子廁所、女賓、男賓、哺乳室等衛生間，還有各自特色地舒適開心。幸福的家呀，溫暖用心、隨處流轉感動。「你們要嘗嘗主恩的滋味，便知道他是美善，投靠他的人有福了。」(詩篇34篇8節)', '臺中市406北屯區崇德路三段1號﹝崇德路與松竹路口﹞', '120.746490', '24.180700', 8.057, '春水堂-朝富店', '朝馬三街與朝富路交叉口不遠處藏身於西屯區，是個名副其實的樂土茶館雖在南來北往的交通要區，但是卻有可以保持鬧中取靜、靜中又取鬧的特殊意境除了交通便利，又加上地理條件優良不僅茶友是相約好地點，也是同事集體出遊的第一站面向潮洋溪，擁有溪景與可散步的悠閒步道右側可說是寧靜與輕鬆鄰近一號國道中港交流道與朝馬轉運站後方則是四通八達左邊緊鄰新市政區與百貨區朝富店可以說是擁有極佳條件兩層樓的建築與開闊的戶外區無論是何時，都極適合來這裡一坐不僅是生活的轉運站更是心靈的補給站吸煙區：一樓戶外座位區\\u3000\\u3000禁煙區：室內全禁煙', '臺中市407西屯區朝馬三街12號', '120.636500', '24.166660', 3.5919, '春水堂-中友店', '春水堂中友店位於台中中友百貨c棟地下二樓櫃位，典雅的設計與空間美感，在中友百貨內獨樹一格。在講求服務的百貨商場內，春水堂的熱情服務多了一種溫暖，親切的招呼則有了溫度。這裡依然有著流水花草，插花掛畫的空間擺設，給環境氛圍帶來了自然的氣息，是都市中缺少的色彩。春水堂一直以來深耕在台中各個角落，這一次在台中最熱鬧的百貨落點，也期許能夠服務更多的茶友。吸煙區：無\\u3000\\u3000禁煙區：室內全禁煙', '臺中市404北區三民路三段161號c棟地下二樓', '120.684750', '24.152070', 1.6066, '春水堂-三越店', '春水堂一直不變的理念，是在日趨功利的速食社會中，能本諸東方傳統文化，依四時冷暖原則，在插花掛畫環境中，經營一家溫馨飲茶館。三越店位於台中市新光三越百貨公司九樓，內部視覺陳設讓人仿若時間倒流，明式風的座席融合東方飲茶的時尚魅力，快速流動的結奏中，能緩慢您的腳步，歇一歇腳，歇一歇心。', '臺中市407西屯區臺灣大道三段301號（新光三越百貨9樓）', '120.647070', '24.164500', 2.4918, '春水堂-國美店', '入駐在國家美術館的春水堂將傳統的茶香、古老的韻味在國際的舞台轉化成賦古且創新的美術品在這裡享受，啜飲甘甜溫馨的飲茶空間欣賞跨時代的展覽吸煙區：無\\u3000\\u3000禁煙區：室內戶外全禁煙', '臺中市403西區五權西路一段2號B1(數位方舟旁)', '120.663510', '24.140940', 2.1286, '春水堂-新時代店', '春水堂新時代店位於台中市後火車站商圈，新時代購物中心2樓；商圈附近文風鼎盛，充滿青春洋溢的活潑氣息!春水堂新時代店呈L型的用餐空間，面向一樓半戶外廣場的落地窗座位有著觀賞活動的最佳視野；綻放梅花的梅枝錯落在店內的各處，呈現出在戶外極富山間大自然氣息處享用美味餐點及道地台灣茶飲的氛圍，「詩寫梅花月，茶烹穀雨春」，新時代店讓您與好友閒聊、客戶商談、家庭聚餐中別有一番清幽的氣氛。吸煙區：無\\u3000\\u3000禁煙區：室內全禁煙', '臺中市401東區復興路四段186號2F（新時代購物中心2F）', '120.687690', '24.136290', 3.0386, '春水堂-育才北店', '在台中市北區‧教育與醫學的精華區原本在中友百貨服務的一群人為了提供更好的場地給更多茶友們在中友百貨A棟側面，拓展了一塊新的樂土親切熱情是我們的服務方式三層樓的超大空間，提供良好的喝茶歡聚空間一樣的品質堅持，不一樣的年輕活力雖然是在台中市最熱鬧的區域仍然一點也不會有擁塞之感這裡有花、有流水、有陽光綠意和美好的音律繚繞最重要的是有好茶相伴，讓飲茶文化不單是冷熱皆宜，男女老少皆愛更多了一份人文味市區樞紐、交通之便轉個彎在春水堂享受您的人間樂土吸煙區：外陽台\\u3000\\u3000禁煙區：室內全禁煙', '臺中市404北區育才北路61號', '120.684450', '24.152990', 1.5333, '春水堂-公益店', '勤美誠品綠園道比鄰台中經國綠園道及市民廣場，與廣大的綠意為伍，感受自然人文氛圍及書香與茶香的自然相遇，無論想要充實你的外在、內在、甚至是味蕾，都可以擁有最輕鬆的選擇體驗貼近夢想的時刻。\\u3000\\u3000春水堂公益店即在勤美誠品為您服務!歡迎您的蒞臨與指教。吸煙區：無\\u3000\\u3000禁煙區：室內全禁煙', '臺中市403西區公益路68號B1樓', '120.663850', '24.151240', 1.1099, 'Top City臺中大遠百', '位於臺中市最重要交通樞紐上的大遠百為全台最大百貨公司，樓上14層、地下2層的超大百貨，結合美食、百貨、量販、精品、娛樂，配合寬敞空間，讓購物不擁塞，除了國際知名精品進駐外，許多知名美食，如鼎泰豐、GODVA、響食天堂等也進駐於此，而以古早傳統台灣味佈置的台灣美食館，讓消費者彷彿回到6、70年代。此外，整棟建築物以綠能為概念，從基地綠化保水、雨水回收，到屋頂設置太陽能發電系統，以及儲冰式空調，也為城市綠建築大樓創立新的示範。(以上資料由台中大遠百提供)', '臺中市407西屯區 臺灣大道三段251號', '120.647070', '24.164500', 2.4918, '中友百貨', '中友百貨自開幕以來，即以「快適生活的提案者」自我期許，提供廣大的消費者一購物休憩的舒適園地。透過每年一到二次的賣場改裝，更將這個理念充份實現。中友百貨帶給消費者更為精緻、豐富、知性、感性兼具的新風貌，打造了一個夢想起飛的百貨新樂園。寬敞明亮的空間、挑高的設計、橫面流暢的動線、以及隨處可見的綠化點，處處都是出於人性化的設計。許多匠心獨具的顧客休息區，茶吧與咖啡吧錯落於各樓層，漫步其間，不購物也舒暢。以敏銳的流行觸角，不斷感應、蒐集世界一流商品。更透過每年的改裝調整，使樓層商品定位更明確，拉近各個客層與時尚舞臺之間的距離，讓流行隨時躍動在生活裡。從一句微笑的「歡迎光臨」開始，我們提供每一位顧客，人性化而全生活的服務。除了一般服務項目外，極少數百貨公司才有的親子廁所、殘障廁所、育兒諮詢室等，更顯現無微不至。深入您心的服務，倍感親切的溫馨，好似在陌生與疏離的人際關係中，縫起一條...', '臺中市404北區三民路三段161 號', '120.684750', '24.152070', 1.6066, '老虎城', '野美國際所投資興建 的Tiger City老虎城購物中心，繼新光三越成功進駐七期新市政中心後，亦將於今年年底進駐七期新市政中心，不但將為七期注入新商機，也為中部地區再添一休閒新去處。 Tiger City購物中心規劃之初，委託AC Nielsen市調公司，針對居住台中市（縣）地區主要商圈15~54歲之男女，進行街頭抽樣訪談，以了解現今消費型態及未來生活趨勢，並以調查結果作為規劃Tiger City購物中心的參考，規劃出符合國際化、人文、藝術、生活、休閒的空間---Tiger City購物中心。', '臺中市407西屯區河南路三段120號', '120.638130', '24.164080', 3.3715, '新光三越百貨公司', '新光三越百貨公司位於臺灣大道上，為台中市大型百貨公司之一，營業內容包括流行服飾、餐飲、UCI派拉蒙環球影城......等，樓層共包括珍饌館 、青春館 、名品館 、國際精品館 、時尚館 、儷人館 、紳士館 、兒童館 、家居生活館 、家庭用品館 、活動館 、文化館 、趣味館 、運動休閒館 、UCI派拉蒙環球影城。一樓戶外廣場並有水舞表演，每個小時都隨著音樂婆娑起舞，也可常見父母帶著小孩興奮得在那兒玩水。為台中市一消費、休閒的好去處。新光三越台中中港店提供中部消費者寬敞舒適的購物娛樂空間，國際精品、各大化妝品品牌、近4千坪的各類女裝、知名3C品牌法雅客、青少年流行品牌旗艦區、生鮮超市、全系列家庭生活賣場…等，另有各國主題美食分層設立，還結合多功能電影城，提供給消費者身、心、靈全面的滿足；此外，我們隨時提供最新流行資訊，讓顧客在一次購足的需求下，享受休閒、藝術、娛樂、資訊…等多...', '臺中市407西屯區臺灣大道三段301號', '120.643710', '24.165260', 2.8435, '黑色古堡-法義風味人文餐廳', '豎立於台中市西區的黑色古堡餐廳，有著中古世紀歐洲城堡的外觀，內部黑、紅相間的裝潢，呈現出神秘、浪漫氛圍，很多情侶在此互許終生，度過浪漫的時刻，是台中著名的求婚、慶生餐廳！ 餐廳供應〈法式料理〉、〈義式料理〉，多年經驗的型男大主廚葉師傅，有著巧思純熟的烹調技巧，堅持只用天然食材，讓您在自在的用餐氣氛中，細細品嚐這美好時刻，將黑色古堡的完美用餐精神推向更積極的顛峰!!', '臺中市403西區大仁街1號', '120.667320', '24.152130', 0.835, '橘光呼嚕貓咪主題餐廳', '悠閒的午後，與貓一起享受著寧靜時光......這裡是有著15隻喵喵的歡樂貓基地～歡迎愛貓族前來 拍貓、玩貓、聊貓經。貓咪‧咖啡‧茶‧焗烤‧咖哩‧手工點心', '臺中市434龍井區藝術街85號1F', '120.595170', '24.187180', 8.3, '琵央卡義式餐廳', '小巧的店面,以簡約的方式,展現出餐廳的樂活,慢食的營運宗旨.食材皆來自主廚親身天然工法種植的安心蔬菜,希望讓每個旅人嚐到最新鮮,最健康的義式風味103年度 東海藝術街商圈優良導覽示範店家102年度台中十大明星商品100年度行政院英語服務標章金質獎94年度臺中市優良旅遊商家', '臺中市434龍井區藝術北街6巷6號', '120.595190', '24.188770', 8.366, '心之芳庭', '愛與幸福的莊園這是一座愛的莊園日日夜夜為愛情而盛放著在約會區裡種下愛情種子在慶典區中採收幸福果實', '臺中市406北屯區民政里芳庭路1號', '120.767490', '24.162310', 9.83, '阿秋廣場', '台中市新地標「阿秋美食廣場」佔地面積900坪，規畫四樓層、每樓層320坪的餐廳，備有專用停車場（44個汽車停車位）及特約停車場（200個汽車停車位），豪華氣派的建築，位在十二期重劃商業區黎明路及台灣大道交叉口，緊臨台中沙鹿交流道以及中彰快速道路的便利性，成為台中市新地標。下台中中港交流道只要三分鐘車程，提供台中市民優質的用餐好去處！', '臺中市407西屯區臺灣大道三段752號', '120.636460', '24.171720', 3.7685, '阿秋大肥鵝宴會廳', '《阿秋大肥鵝餐廳》成立於2005年6月6日，2008年5月喬遷至朝富路旗艦店，為台中海鮮餐廳中多角化經營的另一首席餐廳，並以香港師傅獨門秘方製作的「燒鵝」聞名遐邇。椰林樹影的餐廳外觀，除了在都會生活中創造出舒適的用餐氛圍外，以提供美味、營養、平價的餐飲為己任，並提供您精緻及貼心的服務，是來到大台中必嚐不可的美食餐廳！', '臺中市407西屯區西屯區黎明路三段13號', '120.636680', '24.172070', 3.7626, '格哆莉奶酪優禮', '福品創意食品有限公司~品鮮味佳送禮宴客體面大方台中在地特色伴手禮首選秉持「自然、健康、養生」的三大堅持，致力研發微甜多元化手工鮮奶酪、新鮮水果凍、風味茶凍,法式布丁系列甜點 堅持純手工創意甜點採用台灣在地新鮮食材研製皆無色素香料、無防腐劑；貼心的為消費者提供了第一線的健康品質把關。讓您每口都感受到用心、自然、養生、輕甜讓味蕾綻放甜美的想像，幸福滋味無限蔓延。純手工法式經典甜品法式鮮奶酪系列--奶素鮮嫩滑順口感，獨特創新口味，一口原醇，一口幸福法式布丁系列-- 奶素讓味蕾釋放最原始的感受，享受法國異鄉的浪漫情調風味茶凍系列-- 全素輕甜水嫩的透亮感，享受甜品之餘還多了份養生概念新鮮水果凍系列--全素 晶瑩剔透中帶著實在的果肉，每一口都是新鮮和健康榮獲2016台灣之光百業傑出專業奶酪達人榮獲經濟部商業司【2016食旅台灣味】台灣美食護照榮獲經濟部商業司2015台灣網商節~台...', '臺中市401東區和平街34號', '120.684510', '24.133570', 3.1357, '寶熊漁樂碼頭Okuma Fishing Museum', '寶熊漁樂館 – 展覽‧體驗‧餐飲‧購物「寶熊漁樂館」為全球三大釣具品牌「okuma」寶熊漁具所成立亞洲第一家釣具觀光工廠，延續企業「創造釣魚休閒生活的樂趣」使命，提供釣魚知識、釣具介紹與結合觀光旅遊，成為最具寓教”漁”樂的釣魚殿堂。全館計畫占地1,800坪，涵蓋展覽、體驗、餐飲、購物四大主軸。展覽內容包含釣魚歷史起源、釣場與魚種、品牌故事、釣具產品、釣魚裝備、生產線、檢測室等區塊，兼具文化保留與知識傳承之功能。互動設施種類多樣，有釣遊台灣多媒體、釣魚模擬機、3D海洋影片、4D動感快艇、DIY課程等，適合不同年齡、對象來體驗，咖啡廳設有客席區，可以稍作歇息或談天之用，禮品店與釣具專門店則是提供觀光客與釣魚人不同的購物需求。', '臺中市427潭子區中山路三段11號', '120.706030', '24.219890', 7.6391, '豐饡鐵板燒', '本餐廳鐵板燒台採用NSF合格設備，NSF是世界衛生組織WHO在食品衛生安全領域指定的國際認證機構，鋼板材質皆經過重金屬 ( 鉛、鉻、砷、鎳......等 ) 溶出測試，以保證高溫烹煮急遽熱脹冷縮之過程中，不會釋出各種有害物質。鐵板設備造價為一般市售2～3倍，為的就是讓您吃的安心、吃的健康，豐饡無論在設備、食材上挑選都是替顧客做最嚴格的把關，豐饡用心，所以您放心。(文字節選自 官方網站)', '臺中市407西屯區朝馬路59號', '120.636370', '24.168830', 3.6691, '宜家家居 IKEA', '宜家家居是一家來自於瑞典，具有獨特風格和品牌形象的家具家飾賣場。我們的理想是為大多數人創造更美好的生活，我們希望能不斷提供種類多樣、美觀實用，價格合理，讓大多數人可以負擔的起的家具家飾品。  台中店位於台中市南屯區，鄰近文心森林公園，將提供你更多的居家布置靈感與舒適的購物經驗！', '臺中市408南屯區向上路二段168號', '120.641880', '24.146920', 3.2298, '窩柢咖啡公寓', '一群人窩在老樹根絡裡，呼吸、生活著，享受擁有自己。 窩柢 咖啡公寓', '臺中市407西屯區杏林路27號', '120.642080', '24.167700', 3.0784, 'The Prime-Grill 極炙牛排館', '極致味蕾的美食饗宴 美聲、美食與美酒，是極炙牛排館的代名詞。由台中日月千禧酒店國際廚務團隊展現極致手法，以中西合璧之概念演繹變化出料理新境界。除了料理極致外，本餐廳位於24樓高，坐擁台中市政七期絕佳景致，可將人文薈萃的都會美景盡收眼底。另設有6間包廂，以各國「第一」的數字命名：Yi、Uno、One、Alpha、Odin、Wahed，代表第一，也象徵「極致、最好」，更期許The Prime-Grill 極炙牛排館能成為台中、甚至全台灣最極致的餐飲首選。', '臺中市407西屯區市政路77號24樓', '120.641840', '24.156940', 2.9546, 'Soluna-All Day Dining 饗樂全日餐廳', '豐富多元的亞洲風味美食，採主菜單點的半自助百匯饗宴。', '臺中市407西屯區市政路77號', '120.641840', '24.156940', 2.9546, '路易莎咖啡逢甲福星店', '咖啡、輕食、早午餐', '臺中市407西屯區河南路二段301巷72號', '120.648340', '24.171970', 2.7027, '元波肉圓', '創始於1944年(民國33年)，由第一代(祖父)詹炎波先生稟持傳統古法製作肉圓。雖未有商號，但已打響烏日鄰近鄉間，顧客以(祖父)小名「阿寄」口耳相傳為「烏日阿寄肉圓」那時有可口號「來烏日若不嚐嚐阿寄肉圓，就如同未來過」是鄰里居民常說的老話，直到現在，一直未設商號，到了第二代(母親)詹阿蜂女士在近幾年意識到品牌抬頭的來臨，為了紀念祖父「元」始創作，以名為「波」為商號，於是成立了元波肉圓，繼續為顧客呈現美味點食。', '臺中市414烏日區三民街161號', '120.622230', '24.107520', 7.5398, '元生咖啡', '『次元新生』 以追求真、善、美生活哲學為目標，先求善，進求美 ─ 而後將築構、設計、藝文乃至咖啡，回歸到人與自然的連結。動靜、平衡，真實本質的呈現，源於求真的思維。元生--從生豆引進之後，堅持粒粒手工挑選，剔除受感染及不良瑕疵豆，讓咖啡回到原始的健康與純粹，使自然、風土，真誠表現於咖啡之中，也為守護人們在飲用時的期望。(本篇圖文來自 元生咖啡官網)', '臺中市400中區向上路一段79巷64號', '120.664030', '24.145190', 1.6731, '羅布森書蟲房', '羅布森書蟲房，十年不關的獨立書店一個愛書人的空中樓閣來探索吧！一杯咖啡，一本好書，一段盡情感受文字溫度的午後時光一個只屬於你我的閱讀基地如果您喜歡閱讀、喜歡安靜、不被打擾那這裡就是你的專屬書房，沒有過於吵雜的紛擾只有純粹閱讀的美好歡迎您來我們的閱讀秘密基地─「羅布森 書蟲房」。', '臺中市403西區五權西路一段257號12樓-2', '120.656030', '24.139830', 2.5973, '老舅的家鄉味', '空氣中瀰漫起一股淡淡香氣，沸騰的，除了圓桌上的酸菜白肉鍋，還有聶家老舅一份深切的思鄉之情，團圓的人情味，暖了思鄉人的心。一種道地的風味，一份傳家的至寶，老舅的真情滋味，正宗東北酸菜白肉鍋 ...(本文選自 老舅的家鄉味 官網)', '臺中市401東區忠孝路282號', '120.686560', '24.131410', 3.4435, '屋馬燒肉料亭', '深邃的黑夜，熱情燃起美味炎燒，大紅燈罩下，倚著玻璃窗優雅坐定，黑色沉穩的挑高空間顯得典雅舒適，煩擾的思緒隨著視覺的路線輕輕奔離。愛上，這日本東京現代化的氛圍，藉燒肉與調酒，釋放一身的疲憊 ...(本文取自 屋馬燒肉料亭 粉絲專頁)', '臺中市403西區公益路111號1樓', '120.666350', '24.150720', 1.0186, '紅巢燒肉工房', '一碗白飯。不只是飽食，更是一種享受(本文選自 紅巢燒肉工房 粉絲專頁)', '臺中市408南屯區公益路二段836號', '120.628810', '24.151180', 4.3563, '丰丹嚴選本舖', '一段追尋並實踐夢想、分享美味感動的故事，畢業於中興大學食品科學研究所，任教於學校餐飲專業的創辦人陳老師，因著對各樣食材特性的了解，堅持嚴選來自世界各地的烘焙材料，如美國NP杏仁果、美國蔓越莓、紐西蘭奶油、法國發酵奶油、日本昭和菓子粉等純正食材，傾注對糕餅安全美味的深厚信念，精心製作專屬台灣記憶的美好烘焙。', '臺中市408南屯區大業路277號', '120.648390', '24.153330', 2.364, '台中華美街担仔麵', '台中担仔麵有一種質樸、實在的精神內涵，一種純真的美感。來自台南縣將軍鄉的老闆周文深與周文道兩兄弟，因自小有著漁村的成長背景，對於海鮮料裡有著極高的敏銳度，國中畢業即到台北學習廚藝，歷經多年的學習，1986年到台中創立台中担仔麵，起初是路邊攤，只有六、七桌，專賣担仔麵和海鮮，但來過的客人一吃就上癮，好口碑使它一炮而紅，如今已成為台中高級海鮮的名店。此外，担仔麵也打造佔地1500坪的婚宴會館，內裝展現宮殿式派頭，劇院規格的高級燈光音響，挑高無樑設計的宴會廳可容納上百桌的大型宴會，貼心的服務，尊榮的享受是新人宴會的首選之地。', '臺中市407西屯區華美西街二段215號', '120.665450', '24.167860', 1.1286, 'Passenger 隨食。旅人', '【旅人。常見Q&A】旅人的餐點有許多都是累積自於旅程中的所見所聞，對於第一次來用餐的客人可能會覺得口味上比較特別，為了讓大家有更美好的用餐體驗，在這裡旅人整理了近來客人對於餐點較常會有疑問的部分，如果對於旅人的餐點有其他的問題，也請不吝向服務生詢問，我們都很親切滴！1 燒餅裡那謎樣的紅色物體是？A 是我們手工醃漬的甜菜根！靈感來自於澳洲大漢堡，醃漬法也是和當地人學的，口感特別，和燒餅非常合拍！2 「中東丸子」不是肉？A 不是唷！是由鷹嘴豆搗成的豆泥製成，在國外是一種很普遍的猶太食物，這道在我們老外客人裡可是點閱率No.1！3 奧勒岡沙拉口味好像蠻淡的？A 是的！一般人對於羊肉的印象可能比較偏重口味，但我們的羊肉沙拉搭配的是希臘式醬汁，所以可說是店裡最清爽(清淡？)的一道。若想嘗試羊肉的餐點但怕味道較淡的話，建議可改點燒餅哦！(本文選自Passenger 隨食。旅人 臉書...', '臺中市403西區忠誠街109號', '120.659280', '24.152380', 1.3809, '赤坂屋 日式碳烤燒肉店', '本店開業於 1987到今天也有二十餘年的歷史 由日本師父 木村二郎首先引進台灣 正統日式燒肉的口味 讓人無限回味 歡迎各位到店品嘗 (本文選自 赤坂屋 日式碳烤燒肉店 FB)', '臺中市403西區公益路79號', '120.667320', '24.150640', 0.9867, 'R-Star Coffee', 'R星咖啡.店裡販售的是～對完美的堅持～販售的是~無負擔的舒適空間~.隨便一個角落.都能讓您享有慵懶的一天.......(本文選自  R-Star  粉絲專頁)', '臺中市403西區忠明南路101號', '120.657710', '24.153630', 1.4577, '悅田食品--悅性食物  健康福田', '【悅田食品】\\xad\\xad\\xad五榖堅果專家。「悅性食物、健康福田」，推動悅性素食，創造低碳生活。瑜伽修行者用愛製作健康與喜悅的素食產品。加碼卷優惠 一. 可使用好食卷、藝放券、農遊卷、客庄卷、振興卷二. 購物滿1000元送小麥胚芽、免運宅配，期間:110.11.01~111.04.30止 三. 訂貨電話:0422393183,0930085479   或加LINE！   https://line.me/ti/p/KcDn2JM4LF導航:悅田食品 https://goo.gl/maps/euPjsCEhcwtCskeN9', '臺中市406北屯區軍和街227巷22弄4號', '120.720510', '24.177800', 5.4632, '老阿太和孫女的手工小吃鋪', '老阿太-老闆娘的外婆，93歲老上海人，自祖上習得一手好菜，至今仍終日流連忘返於自家廚房。逢年過節老阿太都會以手工細細製作、用心選料調味，每當絕活好菜上桌時，老人就愛望著孩子津津有味吃著東西的樣子，眼中盡是溫柔，臉上滿是幸福，自此便在老闆娘的腦海中成了熟悉而頑固的故鄉味道。當西化飲食逐漸取代中華飲食裡的深邃滋味，『老阿太和孫女的手工小吃鋪』，呈現了食物最樸直的風味，延續了幼時最珍貴的味蕾記憶。', '臺中市404北區西屯路一段270號', '120.668520', '24.156470', 0.3611, '天廚傳統早點', '創始于1972年,由關中明先生創立,40幾年餐飲經驗,並提供教學授業 (原:南京路157-3號 天廚早點)燒餅，油條，蛋餅，韭菜盒，蔥油餅，高麗菜包，鮮肉包，豆漿，米漿，鹹豆漿...歡迎饕客或團體預訂TEL:04-22131615 Mobile:0933-503-509', '臺中市401東區自由二街92號 (近干城福利廣場)', '120.687720', '24.144580', 2.3405, '這一鍋 皇室秘藏鍋物', '台中朝富殿 預約訂位：04-36090088 門殿位置：台中市西屯區朝富路36號 營業時間：11:30AM ~ 03:00AM台中崇德殿 預約訂位：04-22333308  門殿位置：台中市北屯區崇德路一段596號 營業時間：週一至週五11:30AM~14:00PM、17:00PM~00:00AM                    週六及週日11:30AM~00:00AM', '臺中市407西屯區朝富路36號', '120.637290', '24.166740', 3.5162, 'HUN 混', '沒有魚可以摸，儘管來打混', '臺中市404北區三民路三段114號2樓', '120.684320', '24.149900', 1.698, '目覺三店（mezamashikohi trio）', '一日は目覚ましコーヒーから始める。概念延伸：一日就從喚醒你的咖啡開始! (本文選自 mezamashikohi 粉絲專頁)', '臺中市403西區精誠七街一號', '120.656220', '24.155150', 1.5433, '港町十三番地(雙十店)', '因為愛海和港口，故取名港町十三番地(本文選自台中港町十三番地官網)', '臺中市404北區雙十路223號之1', '120.690120', '24.155970', 1.9878, '小漁兒燒酒雞', '店名充滿戲劇色彩的”小漁兒燒酒雞”，純粹是因為老闆娘很喜歡絕代雙驕中”江小魚”的角色，覺得他非常的豪邁、有趣，便以他的名字命名。(本文選自小漁兒燒酒雞官網)', '臺中市403西區篤行路151號', '120.674330', '24.149330', 1.1229, '食いしん坊', '一間不定時公休、躲在巷子裡很難找菜單又不固定的甜點店(本文選自於食いしん坊官方臉書)', '臺中市402南區五權南路278巷25號', '120.670810', '24.123190', 3.9603, '玩具牧場', '在東海商圈裡有著一間風格獨的遊戲主題餐廳-玩具牧場，在這裡除了提供精緻的餐點外，還有數不清的桌上遊戲讓你可以邊用餐邊歡樂，玩具牧場總是充滿著嘻笑聲，因為到這裡的人除了飽餐一頓外也帶著滿滿歡心與回憶。', '臺中市434龍井區臺灣大道五段3巷42弄17號', '120.592020', '24.182260', 8.4146, '佛羅倫斯義法料理餐廳', '位於臺中理想國藝術街巷弄間，有一間重視義大利文化、藝術及美食的義法料理餐廳，直接以「佛羅倫斯」作為餐廳的名字，無非是嚮往其中的飲食與當地文化。', '臺中市434龍井區藝術街38巷14號', '120.594280', '24.188130', 8.4236, '皮耶小館', '皮耶的外觀是一棟很有南法風格的建築，淡橘色的外牆、藍色的窗框。藍帶科班出身的老闆，堅持提供平價實在的法國料理。雖然菜單上的樣式不多，但店內的料理都是採用天然的食材，完全不含人工添加物所製作的。', '臺中市434龍井區遠東街121號', '120.593440', '24.189760', 8.5727, '台中一中店goûter雅培米堤法式烘焙', '雅培米堤食品有限公司自 2002 年成立以來,始終秉持著「法國味、台灣情」的經營理念；「法國味」指的是堅持使用世界頂級烘培原料與天然的味道,遵循法式手工古法來完成每一項產品,而「台灣情」則是基於對這片土地的熱愛,期望大家都能在沒有經濟負擔之下,享受雅培米堤的甜點。2015 / 11 / 22 在台中市一中商圈開分店了，讓中部愛吃甜點的老饕們不用跑北部在台中也能享用美味甜點，快來台中一中goûter雅培米堤門市選購吧！', '臺中市404北區錦新街83號', '120.684950', '24.153550', 1.5544, '東風雅舍', '東風企業社成立已15年,致力生活美學及慢活人生不遺餘力,骨董家具現代陶藝,日本及台灣名家茶道具及茶人創意服裝,無一不是我們喜愛並精心布置之器物,於此空間與大家分享;二樓並設有茶藝人文空間,供三五好友品茶及談心之天地在此擁有私密小空間可盡情品味中華茶藝之美.', '臺中市403西區五權西三街101號', '120.663160', '24.135090', 2.7549, '隱し藏-向上店', '隱し藏 ， KAKUSIKURA| 當日現流 | 日本料理 | 丼飯專賣 |創始店成立於2011年年底，為台中地區首家以「當日現流魚」主打「海鮮丼飯」聞名的在地美食。提供多款美味丼飯、刺身、握壽司、烤物等日式料理，另有季節限定鍋物、隱藏版美食等，讓愛吃海味的饕客愛不釋手!', '臺中市403西區向上路一段 24號', '120.667340', '24.146850', 1.3859, 'SUGAR & SPICE 糖村旗鑑店', '以禮物分享概念經營的「蛋糕‧禮盒專賣店」，精選來自法國、歐美等食材，搭配台灣當地新鮮特產,期望能以專業、高雅的品牌形象，傳遞屬於糖村的幸福。★2010年獲選為「台北國際花卉博覽會」大會指定伴手禮專門店★2011年獲選為「台中市十大伴手禮首獎」。★2014年獲網友票選為「全世界最好吃的零食TOP10」。★2015年糖村2015年獲台灣金餅獎-太陽餅競賽 金藝獎', '臺中市407西屯區文心路三段357號', '120.666150', '24.173210', 1.65, 'SUAGR & SPICE 糖村崇德店', '以禮物分享概念經營的「蛋糕‧禮盒專賣店」，精選來自法國、歐美等食材，搭配台灣當地新鮮特產,期望能以專業、高雅的品牌形象，傳遞屬於糖村的幸福。★2010年獲選為「台北國際花卉博覽會」大會指定伴手禮專門店★2011年獲選為「台中市十大伴手禮首獎」。★2014年獲網友票選為「全世界最好吃的零食TOP10」。★2015年糖村2015年獲台灣金餅獎-太陽餅競賽 金藝獎', '臺中市406北屯區崇德路二段125號', '120.685320', '24.172670', 2.1163, 'SUAGR & SPICE 糖村福雅店', '以禮物分享概念經營的「蛋糕‧禮盒專賣店」，精選來自法國、歐美等食材，搭配台灣當地新鮮特產,期望能以專業、高雅的品牌形象，傳遞屬於糖村的幸福。★2010年獲選為「台北國際花卉博覽會」大會指定伴手禮專門店★2011年獲選為「台中市十大伴手禮首獎」。★2014年獲網友票選為「全世界最好吃的零食TOP10」。★2015年糖村2015年獲台灣金餅獎-太陽餅競賽 金藝獎', '臺中市407西屯區福雅路103號', '120.619210', '24.185600', 6.0192, 'SUGAR & SPICE 糖村向上店', '以禮物分享概念經營的「蛋糕‧禮盒專賣店」，精選來自法國、歐美等食材，搭配台灣當地新鮮特產,期望能以專業、高雅的品牌形象，傳遞屬於糖村的幸福。★2010年獲選為「台北國際花卉博覽會」大會指定伴手禮專門店★2011年獲選為「台中市十大伴手禮首獎」。★2014年獲網友票選為「全世界最好吃的零食TOP10」。★2015年糖村2015年獲台灣金餅獎-太陽餅競賽 金藝獎', '臺中市408南屯區向上路一段588號', '120.650690', '24.147070', 2.4332, '元祖實業股份有限公司-台中復興店', '「健康、好吃、有故事」是元祖一直以來對產品的堅持，從1981 年元祖第一家店-萬華店的創立，創新的在顧客面前製作麻糬，也於當時掀起了一股熱潮，到現在橫跨台灣及大陸，受到廣大消費者的肯定。元祖不僅傳承中華文化的二十四節氣，並相繼推出綠豆糕、旺來鳳梨酥、銅鑼燒、核棗糕、芝麻糕等產品，另外還有節慶禮盒：春節年糕、端午冰粽、中秋雪餅、常溫自組禮盒等，有節有禮，並讓人與人之間的聯結更緊密；而買的人不吃，吃的人不買，是我們最有趣的顧客寫照。提到元祖，腦海中浮現的不外乎「雪餅、麻糬」，多年來我們秉持著健康且不添加防腐劑的理念，用心經營品牌，提升顧客體驗。', '臺中市402南區復興路三段533號', '120.682680', '24.134520', 2.9613, 'FRajo 法爵雪酪烘焙坊', 'FRajo 法爵 雪酪烘焙坊堅持每日新鮮出爐安心只是我們最基本的承諾', '臺中市400中區柳川里興中街17號', '120.678100', '24.142990', 1.9155, '歐客佬咖啡', 'OKLAO是第一家完全控制咖啡流程的連鎖品牌之一：以咖啡豆的選取、儲存、混合、烘焙、研磨到咖啡的製作，所以步驟都自主獨立完成。我們的咖啡豆來自世界各國的，包含中南美洲、非洲、阿拉伯半島、亞洲等各個產區。OKLAO始終堅持緩慢烘焙工藝，唯有如此才能確保咖啡豆發揮出它最天然的口感和香味。', '臺中市404北區崇德路一段517號', '120.684860', '24.164970', 1.5741, 'FRajo 法爵雪酪冰淇淋\\u3000國光門市', '2016年   520小英國宴唯一指定雪酪冰淇淋品牌FRajo法爵 天然雪酪｜歐式烘焙   品牌理念台灣在歷經食安風暴後，FRajo法爵為讓大家享用天然無負擔的美味，不惜成本以獨特配方與特殊製冰技術，並選用來自新社新鮮白木耳提煉成天然膠質，取代一般人工乳化劑與安定劑，不添加任何防腐劑，低熱量，不含化學添加物質，調和出屬於台灣道地「雪酪」冰淇淋，FRajo法爵讓您吃冰也能吃得很健康。FRajo烘焙，以「天然菌種」養成製作的歐式風格麵包。使用日本鳥越麵粉及法國依思尼產區限定無鹽發酵奶油，我們秉持天然與無化學添加的理念製作麵包，每種食材我們嚴格挑選用心製作，堅持只給您最好的。', '臺中市401東區新民街88號', '120.687950', '24.138380', 2.8663, 'FRajo法爵天然雪酪烘焙坊 青海門市', '嚴選品質 ‧ 天然安心堅持每日新鮮上架！在台中有著『美食戰區』裡，有無數的美食饗宴，照亮台中街頭。而FRajo能在這戰區裡殺出重圍，異軍突起，便是秉持著給人萬分安心與萬分感動的-健康手工冰淇淋♪走一趟FRajo，在這紛亂庸碌的城市，帶給人療癒心靈的感受。', '臺中市407西屯區青海路二段207-18好號', '120.645110', '24.170190', 2.8954, '伊藤麵包工房', '黑糖吐司、芋金香、抹茶日月戀、湯圓吐司、柳橙香菲、巧克力星星、動物餅乾蛋黃酥(預訂製)全手工牛軋糖、餅', '臺中市427潭子區中山路一段101巷8號', '120.701950', '24.193420', 4.9577, '東喜堂', '無', '臺中市427潭子區雅潭路三段東寶巷9號', '120.682570', '24.217660', 6.6117, '三風麵館', '一碗麵，傳遞簡單的美味，更吃入心崁的情感和溫度，麵食專家—三風麵館1999年成立，至今十多年來始終如一，深厚細膩的人情味，傳承自50年代南投霧社的小麵店「民生食堂」。當時，專精的煮麵手藝，湯鮮、味美、料又實在，讓用心處理過的麵條大受歡迎。每日天光微亮，熱氣蒸騰的麵香飄盪於山嵐間，似山間裡吹來的山風，三風名字即由此誕生。', '臺中市428大雅區民富街114號', '120.666670', '24.232990', 8.2121, '熱火美式牛排．Heat Steak．', '(熱火美式牛排)大雅店,以自然美味的風格製作專業的牛排料理，強調健康料理不使用過多的調味醬料，以牛肉的原味來吸引饕客的味蕾。', '臺中市428大雅區民生路一段101號', '120.648600', '24.226820', 7.8498, '布達佩斯冰淇淋', '打造一家具有幸福感的冰淇淋專賣店低油、低糖，天然健康的冰淇淋捨得天天吃，平價又美味的冰淇淋代表「愛情」的玫瑰花瓣造型冰淇淋', '臺中市428大雅區學府路390號', '120.648200', '24.226860', 7.8658, '帝一食補碳燒薑母鴨', '帝一聞香傳千里，美味真心好滋味。歡迎各位好朋友，鬥陣一起來品嚐。', '臺中市428大雅區中清東路78號', '120.648440', '24.221140', 7.2546, '石全石美石鍋專賣店', '全新的美食享受，精心研發韓式新口味，更符合台灣民眾的味蕾!', '臺中市427潭子區興華一路303號', '120.703490', '24.210820', 6.635, '餃先生風味麵館', '原餃先生創意水餃，一直秉持對品質和口味的堅持，以及不斷研發，希望讓愛吃手工水餃的老饕，都能喜愛!餃先生風味麵館是第二代經營的麵館，更是處處用心，選用真材實料，獨家私房料理!', '臺中市427潭子區復興路一段111號', '120.706380', '24.204760', 6.2287, '四月南風\\u3000卡斯提拉', '四月南風的職人遵循日本長崎古法，嚴選天然食材，講究工法與比例掌控，讓卡斯提拉Castela擁有糖發酵如蜜般的濃郁香氣，搭配著新鮮蛋香，緊實濕潤、鬆軟綿密、細緻多層次、甜而不膩的口感，是駐守在秋虹谷旁的美味呈現！', '臺中市407西屯區福科路366號', '120.637480', '24.166790', 3.4988, '新天地東區-瀚熙軒', '瀚熙軒新台菜港式飲茶餐廳位於新天地東區店二樓，提供創新台菜與經典料理，備有各式包廂與2-10人之小吃座位區，適合商務、家庭親友聚會，堪稱台中市東區最具規模與華麗的宴飲空間，讓您面子裡子十足!', '臺中市401東區旱溪東路一段456號二樓', '120.701520', '24.141820', 3.6505, '空海拉麵(日本道地傳統)', '空海拉麵來自日本東京地區，是有著超過十五年歷史的優質品牌。●● (空海拉麵日本總公司) - 在東京當地已有15家分店。空海拉麵以身為日本道地傳統拉麵為傲，引進法國烤骨技術，堅持日本專研的精神，堅持每日熬製的新鮮湯頭。進軍海外亦確保與日本口味同步，原汁原味呈現傳統風味予顧客。最新一家分店設於東京成田國際機場。●●(空海拉麵美國總公司)，則在美國西雅圖大受好評，美國當地已有9 家分店，美國空海並被多次評選為美國推薦優良餐廳。●●(空海拉麵台灣總公司) - 渴望將美味的日式道地拉麵呈現給台灣的饕客們！- 位於台中 ( 西屯區大隆路，1號店。- 位於台中 ( 北屯區崇德路，2號店。1. 主要以提供日式道地原汁原味的拉麵為主，拉麵與沾麵共有約10~15種拉麵2. 美國、台灣等地→ 增加了丼類、日式炸物的選項，強調居酒屋的氛圍，提供消費者更豐富的選擇。3. 美國、台灣等地→ 更增加...', '臺中市407西屯區大隆路140號', '120.648660', '24.158220', 2.2546, 'DK9大坑九號', 'DK9 遠離都市塵囂 紓解身心靈的複合式小桃源大坑九號 一樓 豐私廚 義大利蔬食料理二樓 旭水禪絡 spa三樓 形意瑜珈 教室', '臺中市406北屯區橫坑巷47-9號', '120.745100', '24.178080', 7.839, '三元花園餐廳有限公司', '已經在韓國首爾開店達30年的老店「三元 Garden」,跨海來台,在台北開了一家最頂級,網路人氣也最旺的分店,並在台中也開了分店「三元花園餐廳」,這裡有著寬廣的用餐空間,並與林木相伴,提供傳統的韓式料理,也吸引不少政商名流與影世界的人來到店內用餐。', '臺中市407西屯區臺灣大道四段1962號', '120.604000', '24.184230', 7.3459, \"貓爪子咖啡 Cat's Claw Brunch & Cafe'\", '更多友善寵物資訊請上動保處官網', '臺中市404北區大德街131號', '120.678300', '24.165490', 1.0495, '地芋添糖包心粉圓專賣', '更多友善寵物資訊請上動保處官網', '臺中市406北屯區旅順路二段143號', '120.689780', '24.174250', 2.5654, '逢甲歡樂星', '台中【逢甲歡樂星】引領台灣市集邁向國際化的標竿，集合了多元化的國際美食、提供了趣味動感的遊戲、精緻平價的文創飾品、時尚流行的潮流服飾，以及高規格五星級廁所，食、衣、育、樂一次全都享受到了，二樓更提供超過2百個座位區，不但可以坐下來享用各式美食，還能一邊欣賞精彩的歌唱表演，舒適又美麗的環境能讓您IG、FB一次拍得過癮！想讓朋友們羨慕又忌妒嗎?快來吧! 逢甲歡樂星歡迎您!!', '臺中市407西屯區文華路71號', '120.646470', '24.177520', 3.2188, '大花朵朵主題餐廳(大花朵朵整合行銷有限公司)', '大花朵朵主題餐廳寵物友善，免費提供鮮食吃到飽寬敞的戶外庭院，是毛小孩的天堂樂園!☎️預約專線: (04)22334660地址: 台中市北區學士路98號餐點目錄: https://goo.gl/r4KjpP停車資訊: https://goo.gl/5G8DWB營業時間：10:00-22:00 最後點餐時間 21:00寵物友善餐廳，毛小孩可獲得免費手作鮮食提供wifi、充電座~', '臺中市404北區學士路98號', '120.682760', '24.155300', 1.2778, '森林小徑親子友善寵物餐廳', '義大利麵/燉飯/法式甜點/下午茶鬆餅/早午餐/鍋物提供最天然，健康美味的餐點營業時間10:30-21:00。週四公休台中市北屯區文心路四段131號訂位專線:（04）22982238', '臺中市406北屯區文心路四段131號', '120.675450', '24.173830', 1.7141, '森活，系(森活文創有限公司)', '簡單生活，慢食森活座位有限，建議提早預約文創商品免費寄賣中寵物友善餐廳團體訂位請提前3天預約點餐，以免久候(可透過電話及粉絲專頁訊息留言訂位)', '臺中市407西屯區精誠路50巷35號', '120.655160', '24.156900', 1.6086, '貓老闆咖啡', '我們是以貓咪為主題的寵物咖啡餐廳，這裡有5隻可愛的店貓，店長拿鐵 ，秘書朵朵，膽小蝙蝠俠，調皮忍者龜，人氣王巧虎。每月定期消毒，歡迎大家帶著家裡貓咪一起同樂!!', '臺中市412大里區大里路109號', '120.685900', '24.103340', 6.3465, '安妮廚房', '更多友善寵物資訊請上動保處官網', '臺中市412大里區大里路107號', '120.685850', '24.103370', 6.3421, '水某茶館', '水某以健康為取向，無論烹煮炒炸煎烤，堅持現場烹調， 高湯採用上選昆布大骨，長時間熬製絕不添加味素，讓顧客吃得健康又安心。極具特色的懷舊空間設計，寬敞不壅擠，敬邀您一同來體驗慵懶時光', '臺中市401東區三賢街2號', '120.706100', '24.137350', 4.3094, '順咖啡(順順咖啡)', '在傳承兩代的60年老房子裡，灌溉著巷弄的生活態度，孕育了順咖啡。淺烘焙的咖啡豆，透過簡單而純粹的手沖萃取，蔓延出各具特色的咖啡香氛與果酸韻味，述說著來自世界各產地的故事。坐在順咖啡裡，不論是清爽的拿鐵，或是奔放的耶加雪菲，都能伴著你的心情，演繹著專屬於你與咖啡的美好時光。', '臺中市400中區市府路107巷1-2號', '120.681580', '24.141370', 2.2323, '函館和風火鍋店', '臺中市西屯區福科路591號營業時間：11:00-14:00、17:00-21:00', '臺中市407西屯區福科路591號', '120.613540', '24.186590', 6.5777, 'Gray House灰房子義式餐廳(食恬義式餐廚)', '在這簡單的灰房子裡 藏著不為人知的美食', '臺中市404北區三民路三段201巷30號', '120.684770', '24.153570', 1.5367, '小熊屋中友店(豐鼎興業有限公司)', '凡點餐加1元，享有濃湯，麵包無限量供應以及可任選一杯飲品喔，超值優惠選擇下午兩點到五點，供應甜蜜美味下午茶99元起歡迎來電詢問，04-2225-5157本店焗烤所採用澳洲頂級乳酪絲！！！', '臺中市404北區三民路三段201巷29號', '120.684620', '24.153420', 1.5292, '樂湜餐廳', '我們的店名念 _樂湜(ㄕˊ)_ 湜 ( ㄕˊ) 形容水清澈見底的意思.樂湜提供的餐點不添加味精.雞粉.也不使用化學香料.用心嚴選食材,猶如呵護家人的心', '臺中市402南區工學北路376號', '120.656160', '24.115280', 5.0611, '灰鴿/鍋(禾憶美食館)', '活體波士頓龍蝦 / 天使紅蝦 / 海肥豬蝦 / 大草蝦 / 干貝 / 扇貝 / 帆立貝 / 鮮嫩和牛 / 各部位口感各異的美國牛 / 當日直送王功牡蠣 / 霧峰小農契作米飯 / 台茶18號紅茶 . . . . .', '臺中市408南屯區永春東七路968-3號', '120.633550', '24.151760', 3.8715, '台中亞培米堤法式烘焙(馬丁尼食品有限公司)', '台中gûouter雅培米堤法式烘焙\"超濃超士條\"的美味您一定試試～歡迎來店試吃～地址：台中市北區錦新街83號電話：04-2225-2358', '臺中市404北區錦新街83號', '120.684950', '24.153550', 1.5544, '幸福好食咖啡Homecafe', 'Homecafe是一間以\"寵物認養\"作為宗旨的複合式餐廳, 不同於一般\"寵物餐廳\", 我們是流浪貓狗的\"暫時之家\",目標幫他們找到充滿愛與關懷的永久之家, 所謂\"Homecafe\",是邀請你來我們家作客,聊天和吃飯的同時, 給這些毛孩子親人的機會, 並讓有緣人帶他們回家.我們服務的是\"人\", 所以注重食安, 美味, 整潔,和服務, 同時, 也盼望能幫流浪貓狗與來吃飯的客人牽線, 帶給彼此快樂與愛!', '臺中市404北區興進路58號', '120.697480', '24.155740', 2.7315, '野菜共合國', '蔬食義式料理', '臺中市403西區博館路111號', '120.665350', '24.156210', 0.6341, '一桶tone韓式新食(富帝美食館)', '一桶tone韓式新食專賣韓國燒烤我們是經由炭火去料理每一項食材經典豬五花放上烤盤滋滋作響 油花四濺經典的海鮮鍋裡頭藏著一大隻旭蟹湯頭超鮮美 喝一口回味無窮', '臺中市407西屯區西屯路三段166-60號', '120.613280', '24.190180', 6.7946, '灰鴿/鍋(尚豪美食館)', '波士頓龍蝦 / 麵包蟹 / 三點蟹 / 天使紅蝦 / 海肥豬蝦 / 大草蝦 / 干貝 / 扇貝 / 帆立貝 / 鮮嫩和牛 / 各部位口感各異的美國牛 / 霧峰小農契作米飯 / 當日直送王功牡蠣 . . . . .', '臺中市407西屯區西屯路三段166-72號', '120.612810', '24.190360', 6.8459, '剛好冰菓室(剛好企業有限公司)', '台中市北屯區昌平路一段31號冬季營業時間12-22燒仙草、熱甜湯、鬆餅、烤吐司', '臺中市406北屯區昌平路一段31號', '120.693570', '24.166780', 2.4684, '味無味生活美學飲食空間', '《味無味》專心思考「飲」這件事。專注在草本、全食物、無添加、無咖啡因養生飲品和餐點，打造一個與自然即興演出的空間，讓人和飲品、食器自然對話，感受養生飲的人文、時尚和品味。《味無味》把華人飲食智慧重新找回來、結合現代飲食新知和生活美學，提出全新的飲態度 ～ ☆順時令、用在地     ☆味自然、無添加、品原味       ✩自然簡單就可養身、優雅實用還能養心#素食者友善  #低溫烹調料理  #伴手禮', '臺中市400中區中山路249號', '120.677850', '24.142190', 1.9883, '小惡魔雪莉貝爾彩繪冰棒,蛋糕店', '『小惡魔雪莉貝爾彩繪冰品,蛋糕店』創立人陳汶萱為菖樺食品有限公司第三代接班人所創立，品牌核心價值“創意“為主，改良40餘年傳統枝仔冰加入彩繪元素及小熊外型等新世代思維，品牌名稱”小惡魔“是傳達一種獨特有自信且活潑調皮的個性延伸到產品包裝及整體視覺，”雪莉貝爾“則是創立人英文名加上最喜歡的小熊為名;所以創意冰品皆嚴選自台灣在地食材及獨家專利製冰技術，突破消費者對於傳統枝仔冰印象，『小惡魔雪莉貝爾彩繪冰棒蛋糕店』要挑戰不可能的創意冰品。在 2017 年 9月榮獲臺中市第九屆十大伴手禮雙獎認證“最佳人氣獎“及”好禮標章獎“為本品牌帶來更多注目以及突破冰棒不能成為伴手禮的困境，我們將外包裝及保冰配套措施融入創意及功能性讓消費者送禮自用兩相宜。', '臺中市400中區民族路68號', '120.680220', '24.139250', 2.3811, '陳允寶泉-自由總店', '陳允寶泉自由路總店 百年老店再創新日據時代寶泉第一代陳允先生在豐原現今市區三角街仔賣糕餅。1943年因第二代陳金泉先生在日本所製作的大福麻糬，手工巧、口味實在，所以大受歡迎。陳金泉先生在東京成立【寶泉製果本舖】開創了寶泉的起源。1975年，在豐原糕餅街中正路上成立寶泉本店，由第三代陳增雄先生經營，結合傳統台式與日風的烘焙法，將傳統的月餅加以改良，先後成功研發出小月餅及蛋黃酥，令人耳目一新，立即聲名大噪第四代陳坤宏先生更陸續研發出露之果、日月燒等獨家商品，再創製餅技藝 高峰。多年來榮獲無數優良食品評鑑金牌獎，台中特色商店獎....等等2013年陳允寶泉自由路總店，將原本寶泉的店名上，加上第一代陳允的名字,變成陳允寶泉，表達飲水思源、代代相傳的技術與文化傳承，第四代傳人陳坤宏曾經留學日本研習糕點技術，在加上代代相傳的高深技術，早已成為達人級的糕餅大師，除了不斷根據時代的脈動...', '臺中市400中區自由路2段36號', '120.675610', '24.135370', 2.6561, '騷包 SaoBao Bar&Kitchen', '「當你慾望我的時候，我就在你的呼吸裡」用一句彼此才聽得懂的語句，點一杯特調，騷客乃風雅之人，含蓄、迂迴，低調又放肆。Cocktails調酒 / Draft Beer精釀生啤酒 / Bottled Beer瓶裝啤酒 / Mocktail無酒精飲料 / Snack下酒菜 / #未滿十八歲請勿飲酒 #酒後不開車', '臺中市400中區民族路202號', '120.675720', '24.143110', 1.823, '繼光工務所', '繼光工務所是老宅翻新的建築，集結空間設計、講座、餐飲及展覽的複合空間。', '臺中市400中區繼光街55-1號', '120.681730', '24.138420', 2.529, '路德威餐館', '我們是一群喜愛美食，喜愛歡樂氣氛的店，來自對餐飲的熱誠。希望給大家帶來溫暖的感受', '臺中市403西區公益路36號', '120.668310', '24.150990', 0.9177, '黝脈咖啡', '如果哪裡可以帶你回到過去我一定會選擇黝脈咖啡承載了百年歷史的日治時期街屋推開阻隔了喧囂的厚實木門屋內站滿迎接著訪客的老器材每一個都盛裝著熠熠發亮的新靈魂歷史與文化的脈絡於此凝結成一滴滴的咖啡香燈華初上   黝脈咖啡 歡迎您的光臨', '臺中市400中區成功路253號', '120.679620', '24.143490', 1.9309, '一福堂老店', '源溯到日治昭和三年，一福堂老店創辦人陳周財老師傅，選定緊臨人潮聚集的大墩梅枝町（今竹廣市場中正路上），開創以糕餅專賣的「一福堂菓子舖」，小小店面內不時飄散著四溢的作餅香味，特別是「手工鳳梨酥」的出爐，總是吸引無數過路的生意客與日本大人上門捧場。一福堂「手工鳳梨酥」，乃日據時期最出名的中部糕點，創辦人陳老師傅採用了當時台灣霧峰盛產「旺來」為材料，經反覆的摸索改良，才將土產水果“甘甜呀甘甜”的滋味，巧妙融入其內，橙黃色澤與質樸的在地口味，深深打動眾人的心，很快即成為日據時期一福堂老店的知名代表作。靠著老祖父傳承的好手藝和真材實料、堅持傳統的古早味作餅原則，一福堂老店代代秉持著專職製作道地的「老台中風味名產」為旨。像是民國四十、五十年代，藉由火車兜售傳開的名產「太陽餅」，一福堂老店即以細緻口感令饕客難忘，更扮演起月台零售攤與飛快火車小姐們的大宗供貨商；民國五十三年，結合日本引...', '臺中市400中區臺中市中區中山路67號', '120.682300', '24.138680', 2.5293, '樹合苑', '隱身水泥叢林 自給自在的城市綠洲緊鄰車水馬龍的加油站，另一頭則是霓虹燈閃閃發亮的養生會館，夾在這兩處繁忙空間中，披著草綠色與白色鐵皮的樹合苑靜靜地安坐，低調不起眼的模樣，常讓初次造訪者一不小心就錯過它。但當你踏入一探究竟時，會對眼前的空間感到驚豔不已，手作廚房、閱讀區、咖啡廳、有機商店，還有一座都市中罕見的生態廁所。放眼望去，處處種滿了綠色植物及蔬菜，自給自足的樹合苑，儼然城市中的現代桃花源。', '臺中市404北區中清路一段101號', '120.676800', '24.155420', 0.7215, '喜豐香x審計368  漢式喜餅  喜餅推薦 台中伴手禮', '傳承漢餅的台灣文化、串連起這世代逐漸減少的人情味、 勾起那些似曾相似的味道,兒時珍貴的切下一小塊一人一 口的分著。那麼純真的年代,是這世代遙遠且陌生的記憶。我們賣的不只是餅、與客人之間不只是買賣、也不只是大 日子才能吃到的高貴食品,我們想做的就是成為普通的、 你我都曾經注意過的微小日常。', '臺中市403西區五權西四街七巷15號', '120.661840', '24.139490', 2.3407, '法雅花園冰品甜點', '一個擅長製作焦糖布丁的南投中寮小伙兒戴明其，和一個迷戀法式甜點的台中姑娘何珮嘉，倆人在甜點店相遇、相識、相愛，並將甜點店的甜蜜與浪漫帶回這裡~台中。他們說，用心製作每一道甜點，就是在用心經營他們自己的醇厚香濃的焦糖人生。', '臺中市407西屯區文心路三段357號', '120.666360', '24.173210', 1.6439, 'TSUTAYA BOOKSTORE 台中市政店', '自2003年東京六本木的「TSUTAYA TOKYO ROPPONGI」開始，BOOK&CAFE Style漸漸擴展至日本全國。終於，2017年1月「TSUTAYA BOOKSTORE」首次在台灣展店。書店與Cafe融合在同一個空間中，讓你一邊啜飲香醇咖啡同時挑選書籍，發現自己的Lifestyle。此外，和設於涉谷地標──「SHIBUYA TSUTAYA」中的Cafe Restaurant「WIRED TOKYO」，聯手在一個融合的空間中，打造BOOK&CAFE Style的店舖。我們重視選書的時間及空間，刺激台灣讀者的創意，提供嶄新的閱讀風格及令人雀躍的體驗，希望成為一個能讓眾人喜愛，流連忘返的特別場域。', '臺中市407西屯區市政北二路18之1號2F&3F', '120.642860', '24.160460', 2.8475, '無藏茗茶', '台灣茶葉品牌。文創X電商。O to O茶葉新零售體驗無藏茗茶創立於2009年，以傳承三代的茶葉歷史為基礎。無藏秉持著一份對茶葉的熱愛與執著，加上對環境、生活、美學的熱愛，致力在傳統產業中努力建立新時代環境價值的茶葉品牌。生活，是一件值得用心的事。無藏推廣用心的茶，也推廣用心的生活。「自然簡單」、「高度品質堅持」、「重視人與生活」以及「環境美學」的生活態度與品牌精神，茶葉不再僅是中國的道，日本的禪；茶葉是生活的美,生命的美。「好茶無藏、情意無藏、價格無藏」是無藏一直以來想傳達的品牌思想。我們積極串聯線上與線下的資源，提供給茶友們安全的茶葉原料、來源背景、品茶知識、穩定的價格、環保減量的包裝，更甚至是每週三固定在無藏烏日體驗店舉辦的茶葉分享會，都是無藏希望為台灣茶產業帶來更好的交流。台灣茶擁有得天獨厚的優勢，除了地理及氣候外；更富含悠久的歷史與文化意義。在新舊時代的交替潮流...', '臺中市414烏日區高鐵一路299號2樓', '120.608780', '24.111520', 8.2081, '冒煙的喬美式墨西哥餐廳', '占地150坪的國美店，與台中文化中心、國美館比鄰而居，環境優美充滿文化氣息。冒煙的喬國美店外觀以綠色植物環繞建築，店內裝設、擺飾或傢俱，均來自集團蒐集於各國多年的珍藏品，及卸任餐廳所留下珍貴舊建材，儼然是「冒煙的喬博物館」。此外，冒煙的喬國美店牆上有一個「全台最大的彈珠台」，完全以舊建材及餐具製作，不僅創意十足，也蘊含著「冒煙的喬餐飲集團」濃濃的歷史味。', '臺中市403西區梅川西路一段7號', '120.666710', '24.141610', 1.9653, '舊振南餅店', '舊振南餅店創始於西元1890年（清光緒16年），流淌百年的歲月長河中，我們始終秉持著「喜悅、信任」的精神，藉由手作的精緻漢式糕點，體現漢餅文化的底蘊與傳遞對消費者的尊重與關心。「揉麵要手工、內餡要實在、烤餅火要勻、不加防腐劑」，舊振南是第一個把百年做餅製程寫進祖訓裡的老字號。為符合現代人的口味，舊振南將漢餅精緻化，強調低糖、少油、不添加防腐劑的健康概念，推翻過往大眾對於漢餅多油不健康的印象，受到跨世代喜愛的產品除了經典的綠豆椪、鳳梨酥及漢餅外，還有各式中式糕點及茶類供您喫餅配茶。', '臺中市407西屯區臺灣大道三段301號B2 (臺中新光三越百貨B2)', '120.643710', '24.165260', 2.8435, '五南文化廣場', '來自苗栗擁有50年歷史的「老字號金招牌」，在台中火車站的中山路上開立第一間的實體門市，以販售公職人員、政府出版品與各項考試專用書為書店特色。正統的老書店搭上轉型潮，開設全台灣第一間Food&Book複合式餐廳，請來替高級餐廳規劃空間的名設計師團隊，企圖打造一間美食與書共同交織的知識殿堂;並聘請擁有5星級飯店20多年經驗的創意主廚，承襲高檔餐廳的嚴謹料理步驟製作出一道道美味餐點。 在這極富人文氣息的空間裡，除了美食餐飲外，也包含親子玩樂、拼豆DIY及黏土教學等;您可以拿本好書邊悠閒用餐，小朋友可以盡情玩樂，成為在台中逛書店、熱愛美食及手作學習的好去處。全省共有8家門市，販售各類書籍與文具用品行政院指定的政府出版品總經銷，提供宅配與三大超商取貨服務。', '臺中市400中區中山路6號', '120.683910', '24.137660', 2.7066, '樹太老日本定食-公益創始店', '樹太老堅持日式定食傳統，以平民價美味，創造幸福感動。承蒙廣大美食愛好者青睞與支持，在幾年來讓我們有了一點小小成績，並陸續成立分店，讓更多民眾分享美食。樹太老在此感謝各位的支持，未來將以更積極、更感恩的態度與心情，來面對大家的批評指教，力求進步，以回饋各界的支持!!幸福不在遠處 真味就在樹太老', '臺中市408南屯區公益路二段136-1號', '120.648340', '24.151010', 2.4489, '樹太老日本定食-大墩十九店', '樹太老堅持日式定食傳統，以平民價美味，創造幸福感動。承蒙廣大美食愛好者青睞與支持，在幾年來讓我們有了一點小小成績，並陸續成立分店，讓更多民眾分享美食。樹太老在此感謝各位的支持，未來將以更積極、更感恩的態度與心情，來面對大家的批評指教，力求進步，以回饋各界的支持!!幸福不在遠處 真味就在樹太老', '臺中市407西屯區大墩十九街237號', '120.649860', '24.159230', 2.1314, '樹太老日本定食-台中復興愛買店', '樹太老堅持日式定食傳統，以平民價美味，創造幸福感動。承蒙廣大美食愛好者青睞與支持，在幾年來讓我們有了一點小小成績，並陸續成立分店，讓更多民眾分享美食。樹太老在此感謝各位的支持，未來將以更積極、更感恩的態度與心情，來面對大家的批評指教，力求進步，以回饋各界的支持!!幸福不在遠處 真味就在樹太老', '臺中市402南區復興路一段359號', '120.654340', '24.114700', 5.1794, '樹太老日本定食-台中東山店', '樹太老堅持日式定食傳統，以平民價美味，創造幸福感動。承蒙廣大美食愛好者青睞與支持，在幾年來讓我們有了一點小小成績，並陸續成立分店，讓更多民眾分享美食。樹太老在此感謝各位的支持，未來將以更積極、更感恩的態度與心情，來面對大家的批評指教，力求進步，以回饋各界的支持!!幸福不在遠處 真味就在樹太老', '臺中市406北屯區東山路一段380之12號', '120.731650', '24.176980', 6.4952, '樹太老日本定食-台中文心店', '樹太老堅持日式定食傳統，以平民價美味，創造幸福感動。承蒙廣大美食愛好者青睞與支持，在幾年來讓我們有了一點小小成績，並陸續成立分店，讓更多民眾分享美食。樹太老在此感謝各位的支持，未來將以更積極、更感恩的態度與心情，來面對大家的批評指教，力求進步，以回饋各界的支持!!幸福不在遠處 真味就在樹太老', '臺中市406北屯區文心路四段813號', '120.691530', '24.171680', 2.5326, '哈里歐咖啡蔬食館', '哈里歐咖啡成立於1981年,專營自家烘培精品咖啡豆,商業咖啡豆,義大利咖啡機批發零售,並開闢在台灣的餐飲銷售通路市場,提供咖啡技術教學、披薩餐飲規劃顧問和蔬食咖啡館的多元經營.創辦人對咖啡和蔬食餐飲文化有一份真誠熱愛,因此提倡天然蔬食和咖啡文化,成就哈里歐最大的使命！精緻且養生的咖啡和蔬食,從選購食材、烹飪方式,甚至於空間規劃,哈里歐初衷堅持只賣\"最真,最純,最有溫度的食材\"', '臺中市403西區精誠22街33號1F', '120.656710', '24.147330', 1.9274, '樹太老日本定食-台中青海店', '樹太老堅持日式定食傳統，以平民價美味，創造幸福感動。承蒙廣大美食愛好者青睞與支持，在幾年來讓我們有了一點小小成績，並陸續成立分店，讓更多民眾分享美食。樹太老在此感謝各位的支持，未來將以更積極、更感恩的態度與心情，來面對大家的批評指教，力求進步，以回饋各界的支持!!幸福不在遠處 真味就在樹太老', '臺中市407西屯區青海路二段207-18號 號B1', '120.645070', '24.170240', 2.9014, '樹太老日本定食-台中大里店', '樹太老堅持日式定食傳統，以平民價美味，創造幸福感動。承蒙廣大美食愛好者青睞與支持，在幾年來讓我們有了一點小小成績，並陸續成立分店，讓更多民眾分享美食。樹太老在此感謝各位的支持，未來將以更積極、更感恩的態度與心情，來面對大家的批評指教，力求進步，以回饋各界的支持!!幸福不在遠處 真味就在樹太老', '臺中市412大里區德芳南路487號', '120.681920', '24.104500', 6.1349, '一膳炭造料理鰻魚專賣店 (市政店)', '一膳炭造料理鰻魚專賣店，已經要邁向第9年嘍❗️我們座落在台中市區中，長久一直以來秉持著職人精神，用心為各位製作好每一份餐食。台中最好吃的鰻魚飯 ，堅持嚴選日本百年老店等級白腹鰻。三炭一火、三炭共爐、真火燒烤起火溫度375度 ，炙燒溫度275度，要求最高的雙軟品質。鰻魚鬆軟，入口只需要用舌尖頂至上顎，鰻魚就能化開～白飯Q軟，嚴選來自台東的三冠米王「關山米」！這是一膳每一位職人努力去傳達的信念，給你最好的用餐感受', '臺中市407西屯區市政路567號1F', '120.635010', '24.160590', 3.6449, '北澤壽喜燒-公益店', '來自日本的幸福美味引領台灣壽喜燒風潮的第一品牌壽喜燒(Sukiyaki)，在日本幾乎就等於歡樂與慶祝的代名詞。2007年1月 北澤壽喜燒於台中市公益路成立第一家旗艦店，精選頂級無限制供應的食材，現代化舒適的店內設備以及親切的服務，使北澤壽喜燒一開幕就成為最受中部地區消費者青睞的餐廳之一，並吸引各大媒體報導與網路熱烈討論。', '臺中市408南屯區公益路二段136號', '120.648490', '24.151040', 2.4335, '益家人養生堅果', '門市販售健康無調味養生堅果、牛蒡晶萃養生飲、苦茶油，現場多種禮盒款式供選擇。另有激活遠紅外線能量織品、太陽眼鏡及本草保健食品。Sunnywhole products including natural herbal supplements, nuts, healthy powdered drink, far-infrared ray fabric wear, and Polarized sunglasses, which provide healthcare goods and products.', '臺中市406北屯區崇德二路二段270號', '120.683300', '24.177880', 2.4502, '北澤壽喜燒-大里店', '來自日本的幸福美味引領台灣壽喜燒風潮的第一品牌壽喜燒(Sukiyaki)，在日本幾乎就等於歡樂與慶祝的代名詞。2007年1月 北澤壽喜燒於台中市公益路成立第一家旗艦店，精選頂級無限制供應的食材，現代化舒適的店內設備以及親切的服務，使北澤壽喜燒一開幕就成為最受中部地區消費者青睞的餐廳之一，並吸引各大媒體報導與網路熱烈討論。', '臺中市412大里區德芳南路470號', '120.683140', '24.104630', 6.1448, 'EliubiS愛留彼此霜淇淋體驗店', '源自瑞士阿爾卑斯山區頂級霜淇淋。我們相信，只要懂得關愛自然，尊重生命自然界將會給予我們更多的餽贈。寵物友善環境，同時也是浪浪的中途之家。', '臺中市408南屯區文心路一段480號', '120.646930', '24.151920', 2.5507, '布佬廚房 - 台中新都店', '「Bruce’s Kitchen 布佬廚房」代表著一種追求、落實蔬食生活的新態度觀點，以真誠的料理熱情於2002年創立，多年來秉持著對料理的熱情與堅持，以天然、原味及在地食材為基礎，求新求變，跳脫傳統素食框架，持續以提升精緻健康美味的蔬食與更多人分享。', '臺中市406北屯區和祥路一段121號', '120.726760', '24.173370', 5.9038, '許院', '許願的諧音『許院』- 是希望所有來到這個美好空間人們都可以找到心之所向， 而我們的英文名就叫做 The Wishing House。', '臺中市406北屯區文昌三街 2 號', '120.686540', '24.171290', 2.1018, '樹太老日本定食-台中水湳愛買店', '堅持以美味傳遞幸福的感動樹太老堅持日式定食傳統，以平價美味創造幸福感動，對於食材我們有所堅持，所有食材皆由樹太老主廚嚴選，不管是日本皇室御用的越光米或是達人畜牧精選的優質肉品以及每日新鮮輸送的台灣高麗菜…等，每一份料理、每一瓢醬汁，都是樹太老日本定食對於食材的堅持，更是懷著一份夢想傳遞幸福給消費者的心。幸福不在遠處 真味就在樹太老', '臺中市407西屯區中清路二段1199號水湳愛買B1', '120.659510', '24.192580', 3.8989, '北回木瓜牛奶-逢甲總店', '『在記憶裡不斷提醒著我們，什麼是最美好的事！』_這是一杯木瓜牛奶的意義。夜市裡人潮擁擠，燥熱的手臂不經意地被朋友手上的果飲冰了一下，回過頭，我們相視而笑，那刻是木瓜牛奶的味道，也是北回的初心。我們總是堅信美好並不會隨著長大而遺忘，每當喝一口北回的果飲，就能想起那一刻的笑容，小小一杯飲品，凝聚的是彼此的情感，縮短的是心距離。一顆水果，更讓北回從夜市小攤車慢慢走向回饋社會。我們選擇簡單而謹慎得去做，善待自己的家人，員工，還有合作的果農，堅持提供最好的果飲給消費者。因為我們知道：喝一杯果飲，就能轉動一個美好生活。', '臺中市407西屯區文華路9-10號', '120.645290', '24.175850', 3.2003, '先拼鮮pinfresh', '先拼鮮就是你專屬的農場', '臺中市407西屯區文心路三段183號', '120.659720', '24.171430', 1.7852, '段純貞-廣三Sogo', '經典傳承牛肉麵，獨特秘製23香四川香麻湯頭濃郁順喉，嚴選牛腱心肉，一頭牛只能做成五碗牛肉麵，鮮美肉質Q、嫩、彈！一口咬下美味大爆發，令人再三回味的貨真價實好味道。', '臺中市400中區臺灣大道二段459號14樓', '120.661890', '24.155470', 0.9868, '【曾响號】台灣小吃 古早味美食 雞湯 養生燉湯 傳統滷味', '最貼近你我生活的台灣好味道台灣傳統小吃文化博大精深，不管是香Q的油飯、醇厚鮮美的雞湯還是清湯掛麵都那麼的讓人食指大動，但就是這樣簡單樸實的料理，才能更貼近你我的生活。', '臺中市402南區樹義路61號', '120.652680', '24.110020', 5.7245, '三喜蛋餅', '三喜蛋餅於2011年07月19日創立於台中市三民路與太平路口(一中商圈)，以路邊攤起家，專賣古早味手工蛋餅，堅持開創不同型態之早餐店。從創立至今秉持不廣告、不促銷、不虛假的包裝為原則，只專注於產品本身，我們的每一天只專心做一件事 \" 維持品質,絕不妥協 \"，我們的每一步只希望產品能更加完美，我們相信創造美味的幸福感才是與顧客最好的對話，多一份細心、多一份用心、,多一份堅持、多一份誠信是三喜蛋餅一路走來的核心價值。', '臺中市404北區太平路58號', '120.683110', '24.148520', 1.7002, '沁園春', '沁園春，西元1949年隨國民政府遷台，帶來專屬無錫蔣家的真味細活，傳承江浙菜與上海菜的一脈特色。「沁園春」是由當年中央研究院士吳稚暉先生命名並親筆題字，將詠懷作詩的文人雅宴所感受到的舒暢，比擬團聚分享的美饌饗宴一樣沁入心脾，店址位於台中市中區台灣大道上，歷經70餘年的歲月至今從未搬遷，從政商名流的宴客場所，到凝聚情感的日常家宴，保留了前世紀的飲食記憶，延續來用餐的每一家子獨一無二的美好回憶。至今仍由三房大兒子蔣少炎先生獨資，由第四代生力軍—蔣瓏及郭文章學習經營與傳承。以老麵的基底、堅持每日手工製作銀絲卷和各式蒸餃、鹹、甜包子。招牌菜色沿襲了江浙菜「濃油赤醬」的傳統特色，如寧式鱔糊、河蝦仁、無錫肉骨頭、寧式鱔糊等，深受饕客們的喜愛，也是許多來自日韓、香港、本地的自由行旅客到台中必訪的餐廳，更獲《臺北臺中米其林指南2020》推介的殊榮。', '臺中市400中區臺灣大道一段129號', '120.682660', '24.139520', 2.4647, '裕珍馨/大遠百專櫃', '一首籤詩，六個聖筊，裕珍馨在媽祖的鼓勵下開始了製餅事業，半個世紀以來，從當初的門外漢到今日台灣著名的製餅專家，我們始終一本初衷：「讓愛護我們的人感到與有榮焉」；裕珍馨的餅沒有什麼獨家的秘方，有的只是一顆愛護客戶的心與對材料的堅持，為了滿足前往大甲媽祖廟參拜的信徒及鄉親茹素的需求，裕珍馨改用天然奶油的配方取代傳統的豬油酥餅，不僅成就了今日遠近馳名的「奶油酥餅」，也讓裕珍馨被譽為奶油酥餅的故鄉。', '臺中市407西屯區臺灣大道三段251號B2', '120.644750', '24.164470', 2.7202, '綠野鮮藍帶無花果', '綠野鮮是由兩位小農所組成的台灣在地無花果品牌。無花果早在多年前就有人引進，但因為量產需蓋溫室，成本太高讓許多農民紛紛放棄；原本從事保險業的我們，了解到無花果營養價值最高最能幫助大眾提升健康，毅然決然投入無花果產業。希望種出甜美多汁、賣相好又無毒的無花果，經多次失敗及改良後，終於成功種出綠野鮮藍帶無花果。目前已種植無花果超逾十年，為台灣少許已擁有相當豐富經驗之無花果專業職農。', '臺中市429神岡區中興路29號', '120.690740', '24.241070', 9.3183, '唐太盅養生燉品甜湯 台中公益店', '唐太盅養生燉品甜湯 世上沒有長生之藥，只有盅於養身之道 盅盅都燉煮著用心，碗碗都喝的出元氣 盅湯滋補、甜湯暖脾、膳食與精選十種養身茶飲非常適合現代忙碌工作人飲用。', '臺中市403西區臺灣大道二段161號', '120.668770', '24.151450', 0.8563, '唐太盅養生燉品甜湯 台中中科店', '唐太盅養生燉品甜湯 世上沒有長生之藥，只有盅於養身之道 盅盅都燉煮著用心，碗碗都喝的出元氣 盅湯滋補、甜湯暖脾、膳食與精選十種養身茶飲非常適合現代忙碌工作人飲用。', '臺中市407西屯區永福路172號', '120.621650', '24.185660', 5.8078, '唐太盅養生燉品甜湯 台中大里店', '唐太盅養生燉品甜湯 世上沒有長生之藥，只有盅於養身之道 盅盅都燉煮著用心，碗碗都喝的出元氣 盅湯滋補、甜湯暖脾、膳食與精選十種養身茶飲非常適合現代忙碌工作人飲用。', '臺中市412大里區國光路二段551號', '120.678780', '24.112120', 5.249, '奧兒法低GI輕食餐 台中公益店', '冠軍主廚打造奧兒法低GI輕食餐，完美演繹美味與健康，享受最純粹的滋味', '臺中市403西區臺灣大道二段163號', '120.668710', '24.151170', 0.8878, '奧兒法低GI輕食餐 台中漢口店', '冠軍主廚打造奧兒法低GI輕食餐，完美演繹美味與健康，享受最純粹的滋味', '臺中市404北區漢口路四段367號B1', '120.682870', '24.167210', 1.528, '奧兒法低GI輕食餐 台中五權店', '冠軍主廚打造奧兒法低GI輕食餐，完美演繹美味與健康，享受最純粹的滋味', '臺中市404北區五權路576號', '120.684810', '24.153990', 1.523, '奧兒法低GI輕食餐 台中福科店', '冠軍主廚打造奧兒法低GI輕食餐，完美演繹美味與健康，享受最純粹的滋味', '臺中市407西屯區福康路89號', '120.616900', '24.184940', 6.1905, '奧兒法低GI輕食餐 台中英才店', '冠軍主廚打造奧兒法低GI輕食餐，完美演繹美味與健康，享受最純粹的滋味', '臺中市403西區臺灣大道二段239號B1', '120.666940', '24.152740', 0.793, '隱鍋 台中福科店', '隱鍋提供鍋物料理，有招牌蒜香蛤蜊鍋、柴香檸檬鍋、麻油燒酒鍋、牛奶鍋系列鍋物，養生系列鍋等特色餐點，10多種特色鍋物，邀愛吃鍋的您，大啖隱鍋，美味成癮', '臺中市407西屯區福康路89號', '120.616900', '24.184940', 6.1905, '隱鍋 台中公益店', '隱鍋提供鍋物料理，有招牌蒜香蛤蜊鍋、柴香檸檬鍋、麻油燒酒鍋、牛奶鍋系列鍋物，養生系列鍋等特色餐點，10多種特色鍋物，邀愛吃鍋的您，大啖隱鍋，美味成癮', '臺中市403西區公益路288號', '120.653520', '24.151070', 1.9637, '阿知焢肉 台中黎明店', '黑毛豬手工魯肉飯、香腸，後腿腳庫焢肉飯、手切魯肉，不同一般機器絞肉，一刀一刀手切職人精神，堅持不加任何人工香料味素，讓每一塊焢肉、爌肉賦予舌尖味蕾的感動，入門口迎賓代言人，焢肉魂Achi阿知，讓每一位上門的饕客，滿足口福之慾外，又可享受網紅阿知，討喜可愛的療癒感。', '臺中市407西屯區黎明路三段22號', '120.637080', '24.171600', 3.7051]\n"
          ]
        },
        {
          "output_type": "stream",
          "name": "stderr",
          "text": [
            "INFO:werkzeug:127.0.0.1 - - [21/Oct/2022 04:43:22] \"\u001b[37mPOST / HTTP/1.1\u001b[0m\" 200 -\n"
          ]
        }
      ],
      "source": [
        "#主程序運行\n",
        "app.run()"
      ]
    }
  ],
  "metadata": {
    "colab": {
      "collapsed_sections": [],
      "provenance": [],
      "mount_file_id": "1uLfO9IEeLrZ8pQTxuUHGqj3SFKe5HJSj",
      "authorship_tag": "ABX9TyNb2Pvg1lNaSHJRloGXtxPA",
      "include_colab_link": true
    },
    "kernelspec": {
      "display_name": "Python 3",
      "name": "python3"
    },
    "language_info": {
      "name": "python"
    }
  },
  "nbformat": 4,
  "nbformat_minor": 0
}