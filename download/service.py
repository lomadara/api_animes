from typing import List
from app import db
from flask_sqlalchemy import Pagination
from sqlalchemy import asc, desc
from datetime import datetime
from flask import jsonify
import requests
from bs4 import BeautifulSoup
from urllib.parse import unquote
import time
from tqdm import tqdm
import os


class DownloadService():
    @staticmethod 
    def download(episode_page, resolution):
        try:
            page = requests.get(episode_page)
            soup = BeautifulSoup(page.text, 'html.parser')
            urls = {}
            link1080p = soup.find_all("a", {"class": "btn btn-primary btn-lg"})
            link720p = soup.find_all("a", {"class": "btn btn-info btn-lg"})
            link480p = link480p = soup.find_all("a", {"class": "btn btn-danger btn-lg"})
            epidode_name = ""
            
            for link in link1080p:
                urls['1080'] = 'http://ouo.io/st/wlMjYack/?s='+link['href']
                epidode_name = urls['1080']
            
            if link1080p == []:
                resolution == '720'    
                
                for link in link720p:
                    urls['720'] = 'http://ouo.io/st/wlMjYack/?s='+link['href']
                    epidode_name = urls['720']
            
            if link1080p == [] and link720p == []:
                resolution = '480'    
                
                for link in link480p:
                    urls['480'] = 'http://ouo.io/st/wlMjYack/?s='+link['href']
                    epidode_name = urls['480']
                
            
            total_informations = len(epidode_name.split('/'))
            epidode_name = epidode_name.split('/')[total_informations-3]+ epidode_name.split('/')[total_informations-1].replace('AnV', '')
              
            
            url = ""
            token = ""
            cookie_language = ""
            cookie_session = ""
            attempts = 0
            

            try:
                time.sleep(2)
                announcement_page = unquote(unquote(urls[resolution]))
                page = requests.get(announcement_page)
                soup = BeautifulSoup(page.text, 'html.parser')
                myspans = soup.find_all("span", {"class": "desc"})
                atag = myspans[0].find_all("a")
                soup = BeautifulSoup(page.text, 'html.parser')
                token = soup.find_all("input", {"name": "_token"})
                url = 'https:'+atag[0]['href']
                token = token[0]['value']
                cookie_language = page.cookies['language']
                cookie_session = page.cookies['ouoio_session']
            
                headers = {
                    'Content-type': 'application/x-www-form-urlencoded', 
                    'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9', 
                    'Referer': 'https://ouo.io/go/vf82J', 
                    'cookie': '_ga=GA1.2.2130738344.1596333738; __gads=ID=c2b05018e370b935:T=1596333718:S=ALNI_MZGmQM1lxgFCk68qgdw6QIneJ-rZg; OB-USER-TOKEN=bfc6a841-bcc4-4432-9f92-dcd9dc62e471; adcashufpv3=20117252781448269302437683048; szm_log_id68=qNOKwcyKkorKmpqYyZufmM6czpnJzpGditXe; splash_i=false; __cfduid=d88edece8476a321d427f53f4f582ad531599347948; _gid=GA1.2.1642475669.1599347960; 494668b4c0ef4d25bda4e75c27de2817=1772d66f-f047-4ad7-8396-50c7f77b865c:2:2; ppu_pdc_main_e5e8dd1c9c149a5e60b72911a0f16acf=1; a=cfOz92m00TirkaqGJ1h2h1SNBUU4Vf0b; _popfired=1; _popfired_expires=Invalid%20Date; ppu_pdc_sub_e5e8dd1c9c149a5e60b72911a0f16acf=2; 6US=1; token_QoFDAAAAAAAA-GtSJP36LGpa7Knt_e48oT9UrdI=BAYAX1Vl9wFfVWX3gAGBAcAAIBO3hmhCPMZjJM-eqEwgeKtvCUDAEG3P6HQC5uhoiuMcwQAg_MQ6eKGM1GHgOrB6_CHkLX52YZnT8dRusTN5VDraEuY; token_QpUJAAAAAAAAGu98Hdz1l_lcSZ2rY60Ajjk9U1c=BAYAX1ViggFfVWgGgAGBAsAAIDUXERDDW9BuIninnINjcbiQg0RFEwdKdDZCCrU2KPLcwQBHMEUCIEfJmTkQZrY7ErLGeYLvttyYrIAFT4ML_fOszWwlDPpQAiEAp9Xi1XWT0lYWbBrABANCXHh7FE6nF63G2jONDoBmv_0; lastOpenAt_=1599432712787; _gat=1; _gat_gtag_UA_113932176_25=1; AdskeeperStorage=%7B%220%22%3A%7B%7D%2C%22C911115%22%3A%7B%22page%22%3A8%2C%22time%22%3A1599433026689%7D%7D; ouoio_session='+cookie_session+'; language='+cookie_language
                }
                
                response = requests.post('https://ouo.io/xreallcygo/'+url.split('/')[4], data={'_token': token,'x-token': ''}, headers=headers, stream=True)
                
                
                total_size_in_bytes = int(response.headers.get('content-length', 0))
                block_size = 1024
                progress_bar = tqdm(total=total_size_in_bytes, unit='iB', unit_scale=True)
                os.system('cls')
            
                for data in response.iter_content(block_size):
                    progress_bar.update(len(data))
                    yield data         

            except Exception as exception:
                print(exception, "download_episode")
                attempts += 1

        except Exception as exception:
            print(exception, "obtain_list_of_episodes")