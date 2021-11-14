{
  "nbformat": 4,
  "nbformat_minor": 0,
  "metadata": {
    "colab": {
      "name": "get_matches_api.ipynb",
      "provenance": [],
      "collapsed_sections": [],
      "authorship_tag": "ABX9TyMMJh/G9AUetLHmTxLi8k1t",
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
        "<a href=\"https://colab.research.google.com/github/AminuHabib/sky_bet_league_competition/blob/main/get_matches_api.py\" target=\"_parent\"><img src=\"https://colab.research.google.com/assets/colab-badge.svg\" alt=\"Open In Colab\"/></a>"
      ]
    },
    {
      "cell_type": "markdown",
      "metadata": {
        "id": "omAy_bv3JxZT"
      },
      "source": [
        "Import Libraries"
      ]
    },
    {
      "cell_type": "code",
      "metadata": {
        "id": "DQkjdS9Wkj5y"
      },
      "source": [
        "import requests\n",
        "import json\n",
        "from prettytable import PrettyTable\n",
        "#import sqlite3\n",
        "#import psycopg2\n",
        "#import pandas as pd"
      ],
      "execution_count": 1,
      "outputs": []
    },
    {
      "cell_type": "markdown",
      "metadata": {
        "id": "5my6DPV_J6A1"
      },
      "source": [
        "Create pretty table object"
      ]
    },
    {
      "cell_type": "code",
      "metadata": {
        "id": "gqyUtHpgkkiq"
      },
      "source": [
        "tableobj = PrettyTable()"
      ],
      "execution_count": 2,
      "outputs": []
    },
    {
      "cell_type": "markdown",
      "metadata": {
        "id": "Qd5TK-VaKBZq"
      },
      "source": [
        "API endpoint"
      ]
    },
    {
      "cell_type": "code",
      "metadata": {
        "id": "HYpDhI_Pk7-e"
      },
      "source": [
        "api_endpoint = 'https://feeds.incrowdsports.com/provider/opta/football/v1/matches?compId=10&season=2020'"
      ],
      "execution_count": 3,
      "outputs": []
    },
    {
      "cell_type": "markdown",
      "metadata": {
        "id": "iHOSJTE7KR9c"
      },
      "source": [
        "Fetch data in JSON format"
      ]
    },
    {
      "cell_type": "code",
      "metadata": {
        "id": "aJtdJo9TlSk_"
      },
      "source": [
        "league_data = requests.get(api_endpoint).json()"
      ],
      "execution_count": 4,
      "outputs": []
    },
    {
      "cell_type": "markdown",
      "metadata": {
        "id": "kh9T940PKJUo"
      },
      "source": [
        "Get the status code, returns status value"
      ]
    },
    {
      "cell_type": "code",
      "metadata": {
        "id": "nHlZzUtEJk-B"
      },
      "source": [
        "json_status = league_data['status']"
      ],
      "execution_count": 5,
      "outputs": []
    },
    {
      "cell_type": "code",
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "NP2NrGtljKLT",
        "outputId": "47855aec-66dd-40f3-c218-2d90cb12aa5b"
      },
      "source": [
        "print('API Status: ' + json_status)"
      ],
      "execution_count": 6,
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "API Status: success\n"
          ]
        }
      ]
    },
    {
      "cell_type": "code",
      "metadata": {
        "id": "w_3RZOTomNGi"
      },
      "source": [
        "league_data"
      ],
      "execution_count": null,
      "outputs": []
    },
    {
      "cell_type": "code",
      "metadata": {
        "id": "m-uXOwbypWiV"
      },
      "source": [
        "sky_bet_championship = league_data['data']"
      ],
      "execution_count": 8,
      "outputs": []
    },
    {
      "cell_type": "code",
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "JzSGlumdAnNA",
        "outputId": "b734256a-bc74-4ab3-ada2-e37c8e5e7384"
      },
      "source": [
        "print(type(sky_bet_championship))"
      ],
      "execution_count": 9,
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "<class 'list'>\n"
          ]
        }
      ]
    },
    {
      "cell_type": "markdown",
      "metadata": {
        "id": "tVwVKSF3KiyJ"
      },
      "source": [
        "Store data in Pretty Table"
      ]
    },
    {
      "cell_type": "code",
      "metadata": {
        "id": "MPW8A-zUproZ"
      },
      "source": [
        "for match in sky_bet_championship:\n",
        "    away_team_id = match['awayTeam']['id']\n",
        "    away_team_name = match['awayTeam']['name']\n",
        "    away_team_score = match['awayTeam']['score']\n",
        "    home_team_id = match['homeTeam']['id']\n",
        "    home_team_name = match['homeTeam']['name']\n",
        "    home_team_score = match['homeTeam']['score']\n",
        "    match_id = match['id']\n",
        "    match_period = match['period']\n",
        "    match_competition = match['competition']\n",
        "    match_round = match['round']\n",
        "    match_season = match['season']\n",
        "    match_seasonId = match['seasonId']\n",
        "    match_skyId = match['skyId']\n",
        "    match_status = match['status']\n",
        "    match_type = match['type']\n",
        "    match_venue_id = match['venue']['id']\n",
        "    match_venue_location = match['venue']['location']\n",
        "    match_venue_name = match['venue']['name']\n",
        "\n",
        "    tableobj.add_row([away_team_id, away_team_name, away_team_score, home_team_id, home_team_name, home_team_score, match_id, match_period, match_competition, match_round, match_season, match_seasonId, match_skyId, match_status, match_type, match_venue_id, match_venue_location, match_venue_name])"
      ],
      "execution_count": 13,
      "outputs": []
    },
    {
      "cell_type": "markdown",
      "metadata": {
        "id": "zxNmKCdZKm8K"
      },
      "source": [
        "Create External Field names and assign as column names in Pretty table"
      ]
    },
    {
      "cell_type": "code",
      "metadata": {
        "id": "yFRNx73ByU0X"
      },
      "source": [
        "tableobj.field_names =  ['away_team_id', 'away_team_name', 'away_team_score', 'home_team_id', 'home_team_name', 'home_team_score','match_id', 'match_period', 'match_competition', 'match_round', 'match_season', 'match_seasonId', 'match_skyId', 'match_status', 'match_type', 'match_venue_id','match_venue_location','match_venue_name']"
      ],
      "execution_count": 14,
      "outputs": []
    },
    {
      "cell_type": "markdown",
      "metadata": {
        "id": "Jl4ldz6MopxG"
      },
      "source": [
        "Print first 10 rows of the table"
      ]
    },
    {
      "cell_type": "code",
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "VS4L7xPJGxht",
        "outputId": "4b7bc2db-5015-4e41-8c13-13513bff6104"
      },
      "source": [
        "print(tableobj.get_string(start=0, end=10))"
      ],
      "execution_count": 15,
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "+--------------+---------------------+-----------------+--------------+-------------------+-----------------+--------------------------------------+--------------+----------------------+-------------+------------------+----------------+-------------+--------------+------------+----------------+----------------------+--------------------------------------+\n",
            "| away_team_id |    away_team_name   | away_team_score | home_team_id |   home_team_name  | home_team_score |               match_id               | match_period |  match_competition   | match_round |   match_season   | match_seasonId | match_skyId | match_status | match_type | match_venue_id | match_venue_location |           match_venue_name           |\n",
            "+--------------+---------------------+-----------------+--------------+-------------------+-----------------+--------------------------------------+--------------+----------------------+-------------+------------------+----------------+-------------+--------------+------------+----------------+----------------------+--------------------------------------+\n",
            "|     t25      |    Middlesbrough    |        0        |     t57      |      Watford      |        1        | 7af1fb87-75e5-322a-94f0-8298e87e8e14 |  Full Time   | Sky Bet Championship |      1      | Season 2020/2021 |      2020      |    429715   |    result    |  Regular   |       73       |       Watford        |            Vicarage Road             |\n",
            "|     t94      |      Brentford      |        0        |     t41      |  Birmingham City  |        1        | a73e9fb4-d61e-34f4-9788-a0049ae68980 |  Full Time   | Sky Bet Championship |      1      | Season 2020/2021 |      2020      |    429706   |    result    |  Regular   |       57       |      Birmingham      | St. Andrew's Trillion Trophy Stadium |\n",
            "|     t72      |   Rotherham United  |        1        |     t112     | Wycombe Wanderers |        0        | fd69d98c-692e-3e30-a686-04dec22a447f |  Full Time   | Sky Bet Championship |      1      | Season 2020/2021 |      2020      |    429716   |    result    |  Regular   |       3        |       Wycombe        |              Adams Park              |\n",
            "|     t102     |      Luton Town     |        1        |     t37      |      Barnsley     |        0        | 1f14aa09-f9e0-3840-80c8-10e98878ffb9 |  Full Time   | Sky Bet Championship |      1      | Season 2020/2021 |      2020      |    429705   |    result    |  Regular   |       53       |       Barnsley       |               Oakwell                |\n",
            "|      t5      |   Blackburn Rovers  |        2        |     t91      |    Bournemouth    |        3        | bcfb84b7-b264-3136-a415-778769e708fa |  Full Time   | Sky Bet Championship |      1      | Season 2020/2021 |      2020      |    429707   |    result    |  Regular   |      2734      |     Bournemouth      |           Vitality Stadium           |\n",
            "|      t9      |    Coventry City    |        1        |     t113     |    Bristol City   |        2        | 2cd27cdc-e4e6-3bcf-8895-112a90f3d1e5 |  Full Time   | Sky Bet Championship |      1      | Season 2020/2021 |      2020      |    429708   |    result    |  Regular   |       4        |       Bristol        |             Ashton Gate              |\n",
            "|     t19      | Sheffield Wednesday |        2        |     t97      |    Cardiff City   |        0        | 5c59cdb4-b377-3aaa-a019-8ec25a2feddb |  Full Time   | Sky Bet Championship |      1      | Season 2020/2021 |      2020      |    429709   |    result    |  Regular   |      5040      |       Cardiff        |         Cardiff City Stadium         |\n",
            "|     t45      |     Norwich City    |        1        |     t38      | Huddersfield Town |        0        | 402cacb7-f454-365c-8ff4-42932f0735a8 |  Full Time   | Sky Bet Championship |      1      | Season 2020/2021 |      2020      |    429711   |    result    |  Regular   |       54       |     Huddersfield     |         John Smith's Stadium         |\n",
            "|     t110     |      Stoke City     |        0        |     t103     |      Millwall     |        0        | 4af84d36-cfed-3ebb-99f3-6d2f8e13a6c9 |  Full Time   | Sky Bet Championship |      1      | Season 2020/2021 |      2020      |    429712   |    result    |  Regular   |      101       |        London        |               The Den                |\n",
            "|     t80      |     Swansea City    |        1        |     t107     | Preston North End |        0        | 7790874d-0cc2-35db-a68d-c2a2c8eb625d |  Full Time   | Sky Bet Championship |      1      | Season 2020/2021 |      2020      |    429713   |    result    |  Regular   |      105       |       Preston        |               Deepdale               |\n",
            "+--------------+---------------------+-----------------+--------------+-------------------+-----------------+--------------------------------------+--------------+----------------------+-------------+------------------+----------------+-------------+--------------+------------+----------------+----------------------+--------------------------------------+\n"
          ]
        }
      ]
    },
    {
      "cell_type": "markdown",
      "metadata": {
        "id": "IQkpaNTFK-fc"
      },
      "source": [
        "Store data in Text File format"
      ]
    },
    {
      "cell_type": "code",
      "metadata": {
        "id": "6OykhDl22rau"
      },
      "source": [
        "league_data_text = tableobj.get_string()"
      ],
      "execution_count": 16,
      "outputs": []
    },
    {
      "cell_type": "code",
      "metadata": {
        "id": "CTjybzdP2_zL"
      },
      "source": [
        "filename = 'Sky_competition.txt'"
      ],
      "execution_count": 17,
      "outputs": []
    },
    {
      "cell_type": "code",
      "metadata": {
        "id": "AhgAfH3N20tf"
      },
      "source": [
        "with open(filename, 'w') as file: \n",
        "    file.write(league_data_text)"
      ],
      "execution_count": 19,
      "outputs": []
    }
  ]
}