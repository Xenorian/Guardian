from flask import Flask, request, jsonify, url_for

from flask_cors import CORS

from werkzeug.utils import secure_filename
from urllib.parse import urlparse, unquote

import os
import threading
from pathlib import Path

import requests
import json

STATIC_FOLDER = '/root/amax-volume/static/'

lock = threading.Lock()

app = Flask(__name__,static_folder=STATIC_FOLDER)
video_idx = 0
image_idx = 0
CORS(app)  # 启用全局 CORS

def get_next_index(directory_path):
    # 初始化最大索引为 0
    max_index = 0
    
    # 遍历文件夹中的所有文件
    for filepath in Path(directory_path).iterdir():
        # 仅处理文件，不处理目录
        if filepath.is_file():
            # 分割文件名，提取出数字部分
            try:
                # 假定文件名为 '1.jpg', '2.png' 等格式
                index = int(filepath.stem)  # stem 是不带扩展名的部分
                if index > max_index:
                    max_index = index
            except ValueError:
                # 如果文件名不符合我们期望的格式，继续处理下一个
                continue
    
    # 返回最大的索引加一
    return max_index + 1


video_idx = get_next_index(os.path.join(STATIC_FOLDER, 'videos'))
image_idx = get_next_index(os.path.join(STATIC_FOLDER, 'images'))


@app.route("/field/getFieldRule", methods=['POST'])
def getFieldRule():
    # rule = {
    #     29: "Ensure that this person is wearing a full police uniform, including a shirt and pants, for both the upper and lower body, rather than casual clothing",
    #     30: "Ensure that no police officer is trading stocks, playing cards, playing mobile games, or watching entertainment videos in the office area",
    #     31: "Ensure that no police officers gather to chat, sleep or doze off during daytime working hours",
    #     32: "Ensure that there is always someone on duty at the window position during daytime working hours, and that no police officers leave their posts without permission in the presence of the public",
    #     33: "Ensure that the relevant police equipment is neatly placed in the correct position after the staff leave, and must not be placed arbitrarily",
    #     34: "This is a scene from an interrogation room,  Just need to ensure that there are two uniformed police officers present",
    #     35: "This is a surveillance footage of the police carrying the suspect to the detention center. It must be ensured that there are two police officers wearing police uniforms in the footage, one on the left and one on the right, carrying the suspect",
    #     36: "Please ensure that the staff do not engage in the behavior of drinking beverages, milk tea, or snacking",
    #     37: "This is the police station studio. Please make sure no one is smoking. Please note that any behavior of holding a cigarette in your hand or smoking with your mouth is considered smoking",
    #     38: "Ensure that the doors of the case handling area, storage room, and gun depot are not left open for a long time",
    #     39: "Ensure that the suspect's hands and feet are securely locked during interrogation",
    #     40: "This is a scene inside the detention center, with a bed on the left and a floor on the right. Please ensure that the people inside (prisoners) are not allowed to stand on the bed"
    # }
    rule = {
        29: "确保该人员穿着完整的警服，包括上衣和裤子，而不是休闲服装",
        30: "确保没有警察在办公区域内炒股、打牌、玩手机游戏或观看娱乐视频",
        31: "确保没有警察在白天工作时间聚集聊天、睡觉或打瞌睡",
        32: "确保在白天工作时间内窗口位置始终有人值班，并且没有警察在公众面前未经允许离开岗位",
        33: "确保工作人员离开后，相关警用装备整齐地放在正确的位置，不得随意放置",
        34: "这是审讯室的场景，只需确保现场有两名穿制服的警察在场",
        35: "这是警察将嫌疑人带往拘留中心的监控画面。必须确保画面中有两名穿警服的警察，一名在左边，一名在右边，共同携带嫌疑人",
        36: "请确保工作人员不要出现喝饮料、奶茶或吃零食的行为",
        37: "这是派出所工作室，请确保没有人吸烟。请注意，手持香烟或口中吸烟均被视为吸烟行为",
        38: "确保办案区、储藏室和枪库的门不长时间敞开",
        39: "确保在审讯过程中嫌疑人的手脚被安全锁住",
        40: "这是拘留中心内的场景，左侧有一张床，右侧是地面。请确保里面的人（囚犯）不允许站在床上"
    }

    output = []
    for idx, (k, v) in enumerate(rule.items()):
        tmp = dict()
        tmp['index'] = idx
        tmp['id'] = k
        tmp['text'] = v
        output.append(tmp)

    return output

# 设置允许上传的文件扩展名
ALLOWED_EXTENSIONS = {'png', 'jpg', 'jpeg'}
# 假设图片存储在 static/images 目录下
IMAGE_FOLDER = 'images'

def allowed_file(filename):
    return '.' in filename and \
           filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

@app.route('/task/uploadImg', methods=['POST'])
def upload_file():
    global image_idx

    # 检查是否有文件被上传
    if 'file' not in request.files:
        return jsonify({'error': 'No file'}), 400
    file = request.files['file']
    # 如果用户没有选择文件，浏览器也会提交一个空的部分，没有文件名
    if file.filename == '':
        return jsonify({'error': 'No selected file'}), 400
    if file and allowed_file(file.filename):
        filename = file.filename
        filename = "{}{}".format(image_idx, os.path.splitext(filename)[1])
        with lock:
            file.save(os.path.join(os.path.join(app.static_folder, IMAGE_FOLDER), filename))  # 替换为你的文件保存路径
            image_idx += 1
        return jsonify({'success': True, 'filename': filename}), 200
    else:
        return jsonify({'error': 'File type not allowed'}), 400


@app.route('/task/getImg', methods=['POST'])
def get_imgs():
    # 获取图片目录的绝对路径
    image_dir = os.path.join(app.static_folder, IMAGE_FOLDER)
    
    # 检查目录是否存在
    if not os.path.isdir(image_dir):
        return jsonify({'error': 'Image directory not found'}), 404
    
    # 遍历目录中的所有文件，获取图片文件名
    images = [f for f in os.listdir(image_dir) if os.path.isfile(os.path.join(image_dir, f))]
    images = sorted(images)
    # 生成每张图片的 URL
    image_urls = [url_for('static', filename=f'{IMAGE_FOLDER}/{img}') for img in images]
    
    # 返回 JSON 格式的图片 URL 列表
    return image_urls

@app.route('/task/del', methods=['POST'])
def del_things():
    # 获取 POST 请求中的 JSON 数据
    data = request.get_json()
    if data is None:
        return jsonify({"error": "No JSON data provided"}), 400

    url = data.get('url')
    if url is None:
        return jsonify({"error": "'url' not provided"}), 400
    
    # 解析 URL，提取路径部分
    parsed_url = urlparse(url)
    relative_path = unquote(parsed_url.path.lstrip('/'))
    path_parts = relative_path.split(os.sep)
    path_parts[0] = app.static_folder
    new_path = os.sep.join(path_parts)

    
    # 安全校验，确保文件在 static 下
    # 定义基目录和文件路径
    base_dir = os.path.abspath(app.static_folder)
    file_path = os.path.abspath(new_path)

    # 校验文件路径是否在基目录下
    if not file_path.startswith(base_dir + os.sep):
        return jsonify({'status': 'error', 'message': 'Invalid file path.'})
    
    # 尝试删除文件
    try:
        with lock:
            os.remove(file_path)

        return jsonify({'status': 'success', 'message': f'Image {url} deleted.'})
    except FileNotFoundError:
        return jsonify({'status': 'error', 'message': 'File not found.'})
    except Exception as e:
        return jsonify({'status': 'error', 'message': f'Failed to delete image: {str(e)}'})

ALLOWED_VIDEO_EXTENSIONS = {'mp4', 'avi', 'mov'}
VIDEO_FOLDER = 'videos'

def allowed_video_file(filename):
    return '.' in filename and \
            filename.rsplit('.', 1)[1].lower() in ALLOWED_VIDEO_EXTENSIONS

@app.route('/task/uploadVideo', methods=['POST'])
def upload_video():
    global video_idx
    # 检查是否有文件被上传
    if 'file' not in request.files:
        return jsonify({'error': 'No file provided'}), 400
    file = request.files['file']
    # 如果用户没有选择文件，浏览器也会提交一个空的部分，没有文件名
    if file.filename == '':
        return jsonify({'error': 'No selected file'}), 400
    if file and allowed_video_file(file.filename):
        filename = file.filename
        print(filename)
        print(os.path.splitext(filename))
        filename = "{}{}".format(video_idx, os.path.splitext(filename)[1])
        with lock:
            file.save(os.path.join(app.static_folder, VIDEO_FOLDER, filename))  # 替换为视频文件夹路径
            video_idx += 1
        return jsonify({'success': True, 'filename': filename}), 200
    else:
        return jsonify({'error': 'File type not allowed'}), 400


@app.route('/task/getVideo', methods=['POST'])
def get_videos():
    # 获取视频目录的绝对路径
    video_dir = os.path.join(app.static_folder, VIDEO_FOLDER)
    
    # 检查目录是否存在
    if not os.path.isdir(video_dir):
        return jsonify({'error': 'Video directory not found'}), 404
    
    # 遍历目录中的所有文件，获取视频文件名
    videos = [f for f in os.listdir(video_dir) if os.path.isfile(os.path.join(video_dir, f))]
    videos = sorted(videos)
    # 生成每个视频的 URL
    video_urls = [url_for('static', filename=f'{VIDEO_FOLDER}/{video}') for video in videos]
    
    # 返回 JSON 格式的视频 URL 列表
    return video_urls

@app.route('/task/imgInference', methods=['POST'])
def img_inference():
    # 获取 POST 请求中的 JSON 数据
    data = request.get_json()
    if data is None:
        return jsonify({"error": "No JSON data provided"}), 400

    rule_list = data.get('rule_list')
    if rule_list is None:
        return jsonify({"error": "'rule_list' not provided"}), 400


    url = "http://127.0.0.1:5555/test_demo"
    # 准备请求头和数据
    headers = {
        "Content-Type": "application/json"
    }
    data = {
        "dataset_dir": "/home/wxy/docker-volume/static/images",
        "rule_list": rule_list,
        "image_type": "police office" 
    }
    # 发送 POST 请求
    response = requests.post(url, headers=headers, data=json.dumps(data))

    if response.status_code == 200:
        return jsonify({'success': True, 'data': response.text}), 200
    else:
        return jsonify({"error": "api error " + response.text }), 400

@app.route('/task/videoInference', methods=['POST'])
def video_inference():
    # 获取 POST 请求中的 JSON 数据
    data = request.get_json()
    if data is None:
        return jsonify({"error": "No JSON data provided"}), 400

    rule_list = data.get('rule_list')
    if rule_list is None:
        return jsonify({"error": "'rule_list' not provided"}), 400
    
    video_url = data.get('video_url')
    if video_url is None:
        return jsonify({"error": "'video_url' not provided"}), 400

    parsed_url = urlparse(video_url)
    relative_path = unquote(parsed_url.path.lstrip('/'))
    
    path_parts = relative_path.split(os.sep)
    path_parts[0] = '/home/wxy/docker-volume/static'
    new_path = os.sep.join(path_parts)
    
    url = "http://127.0.0.1:6666/chatVideo"
    # 准备请求头和数据
    headers = {
        "Content-Type": "application/json"
    }
    data = {
        "video_dir": new_path,
        "rule_list": rule_list,
    }
    # 发送 POST 请求
    response = requests.post(url, headers=headers, data=json.dumps(data))

    if response.status_code == 200:
        return jsonify({'success': True, 'data': response.text}), 200
    else:
        return jsonify({"error": "api error " + response.text }), 400