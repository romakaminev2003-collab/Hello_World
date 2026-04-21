{
  "nbformat": 4,
  "nbformat_minor": 0,
  "metadata": {
    "colab": {
      "provenance": [],
      "authorship_tag": "ABX9TyPS3k6RM0akRKa8o/VmTMXJ",
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
        "<a href=\"https://colab.research.google.com/github/romakaminev2003-collab/Hello_World/blob/main/%D0%9F%D1%80%D0%B0%D0%BA%D1%82%D0%B8%D1%87%D0%B5%D1%81%D0%BA%D0%BE%D0%B5_%D0%B7%D0%B0%D0%B4%D0%B0%D0%BD%D0%B8%D0%B5_10_5.py\" target=\"_parent\"><img src=\"https://colab.research.google.com/assets/colab-badge.svg\" alt=\"Open In Colab\"/></a>"
      ]
    },
    {
      "cell_type": "code",
      "execution_count": 40,
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "S1p0pZs6CHp9",
        "outputId": "53af6dd4-274d-4b0e-a713-d3d434477ab4"
      },
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "1) Среднее количество просмотренных страниц: 17.486992715920916\n",
            "2) Стандартное отклонение: 1442.7984472210853\n",
            "3) Высокая вариабельность: 82.50695077533251\n",
            "4) Есть статистически значимая разница в количестве страниц: 0.00013741248854821084\n"
          ]
        }
      ],
      "source": [
        "import pandas as pd\n",
        "from scipy import stats\n",
        "\n",
        "\n",
        "def website_analyse(file_name):\n",
        "    df = pd.read_csv (file_name)\n",
        "    mean = df['Просмотренные страницы'].mean()\n",
        "    std = df['Время на сайте (сек)'].std()\n",
        "    cv = std/mean\n",
        "    df_mobile = df[df['Тип устройства'] == 'Мобильное']\n",
        "    df_desktop = df[df['Тип устройства'] == 'Десктоп']\n",
        "    stat, p_value = stats.ttest_ind(df_mobile['Просмотренные страницы'], df_desktop['Просмотренные страницы'])\n",
        "\n",
        "\n",
        "    print (f'1) Среднее количество просмотренных страниц: {mean}')\n",
        "    print (f'2) Стандартное отклонение: {std}')\n",
        "    if cv > 0.25:\n",
        "        print (f'3) Высокая вариабельность: {cv}')\n",
        "    elif cv <= 0.25 and cv > 0.1:\n",
        "        print (f'3) Умеренная вариабельность: {cv}')\n",
        "    else:\n",
        "        print (f'3) Слабая вариабельность: {cv}')\n",
        "\n",
        "    if p_value < 0.05:\n",
        "        print (f'4) Есть статистически значимая разница в количестве страниц: {p_value}')\n",
        "    else:\n",
        "        print (f'4) Нет статистически значимой разницы: {p_value}')\n",
        "\n",
        "website_analyse ('website_visits_december_2024.csv')"
      ]
    }
  ]
}