import re
import requests
import zipfile
from pathlib import Path
from pathlib import PosixPath
from matplotlib import font_manager
import os
import re
import shutil
from glob import glob
from matplotlib import matplotlib_fname
from matplotlib import get_cachedir
import matplotlib.pyplot as plt 
from matplotlib import cycler

def is_valid_url(url: str) -> bool:
  regex = re.compile(
          r'^(?:http|ftp)s?://' # http:// or https://
          r'(?:(?:[A-Z0-9](?:[A-Z0-9-]{0,61}[A-Z0-9])?\.)+(?:[A-Z]{2,6}\.?|[A-Z0-9-]{2,}\.?)|' #domain...
          r'localhost|' #localhost...
          r'\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3})' # ...or ip
          r'(?::\d+)?' # optional port
          r'(?:/?|[/?]\S+)$', re.IGNORECASE)
  return re.match(regex, url) is not None


def download_font(font_url: str, local_font_folder_path: PosixPath = Path("utils/") / "fonts" , local_font_name: str="my_downloaded_font.ttf") -> None:
  if not is_valid_url(font_url):
    raise ValueError('font_url is not a valid url')

  if local_font_folder_path.is_dir():
      print(f"{local_font_folder_path} directory exists.")
  else:
      #print(f"Did not find {local_font_folder_path} directory, creating one...")
      local_font_folder_path.mkdir(parents=True, exist_ok=True)
      
  # Download 
  with open(local_font_folder_path / local_font_name, "wb") as f:
      request = requests.get(font_url)
      #print("Downloading font...")
      f.write(request.content)


def install_matplotlib_font_from_local_file(font_path,matplotlib_fontname ) -> None:
  font = font_manager.FontEntry(fname=font_path, name=matplotlib_fontname)
  font_manager.fontManager.ttflist.append(font)


def install_matplotlib_font_from_url(font_url: str, local_font_name: str, local_font_folder_path: PosixPath = Path("utils/") / "fonts") -> None:
  local_font_name_with_extension = local_font_name + '.ttf'
  print(f"{local_font_name_with_extension=}")
  download_font(font_url, local_font_folder_path, local_font_name_with_extension )
  font_path = str(local_font_folder_path) + '/' + local_font_name_with_extension 
  print(f"{font_path=}")
  install_matplotlib_font_from_local_file(font_path,local_font_name )


FIRA_CODE_FONT_URLS = {
    "regular": "https://www.dropbox.com/scl/fi/80fie38nk0cfl8l98oc3v/FiraCode-Regular.ttf?rlkey=jttpj4oy3f4qpeu9376oj5hnd&dl=1",
    "bold": "https://www.dropbox.com/scl/fi/vrc9bdldyqsdfrli6s5mt/FiraCode-Bold.ttf?rlkey=5td077dq51uajc1cecp00qw84&dl=1",
    "light": "https://www.dropbox.com/scl/fi/j7hjgy3u9d85qneebe7ub/FiraCode-Light.ttf?rlkey=4v2914rm6z4ex6v6f1xar0zoy&dl=1",
    "medium": "https://www.dropbox.com/scl/fi/ygxi8r4m1mpurtn4sjjkq/FiraCode-Medium.ttf?rlkey=v29mott5vgbugm4o36l9cx76s&dl=1",
    "semibold": "https://www.dropbox.com/scl/fi/wyro7qus4eyfh2btcywcq/FiraCode-SemiBold.ttf?rlkey=61xciephwwq9jumralub6m1f9&dl=1"
    }

def install_fonts():
  install_matplotlib_font_from_url(FIRA_CODE_FONT_URLS["regular"], "firacode_regular")   
  install_matplotlib_font_from_url(FIRA_CODE_FONT_URLS["bold"], "firacode_bold")                          
  install_matplotlib_font_from_url(FIRA_CODE_FONT_URLS["semibold"], "firacode_semibold")   
  install_matplotlib_font_from_url(FIRA_CODE_FONT_URLS["light"], "firacode_light") 
  install_matplotlib_font_from_url(FIRA_CODE_FONT_URLS["medium"], "firacode_medium") 




def set_default_rcparams():
    install_fonts()
    skyblue = '#87CEEB'
    red = '#FF7777'
    violet = '#AA99EE'
    yellow =  '#FFDD66'
    colors = cycler('color', [skyblue, red, violet, yellow,'#3388BB' ,'#88BB44', '#FFBBBB'])
    plt.rc('axes', edgecolor='black', axisbelow=True, grid=True, prop_cycle=colors,linewidth=0.5)
    plt.rc('font', family='firacode_light' )
    plt.rc('grid', color='lightgray', linestyle='--')
    plt.rc('lines', linewidth=1)
    plt.rc('figure', dpi= 300)
    plt.rc('legend', frameon=False, facecolor= '#FFFFFF')
