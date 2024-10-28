// src/api/api.ts
import axios from 'axios';
import type { AxiosInstance, InternalAxiosRequestConfig, AxiosResponse } from 'axios';

export const BASE_URL = 'http://127.0.0.1:5000'; // 替换为你的后端 API 基础 URL
// const BASE_URL = 'http://10.82.77.153:5000'; // 替换为你的后端 API 基础 URL

const GET_FIELD_RULE_ENDPOINT = 'field/getFieldRule'
const UPLOAD_IMAGE_ENDPOINT = 'task/uploadImg'
const GET_IMAGE_LIST_ENDPOINT = 'task/getImg'
const UPLOAD_VIDEO_ENDPOINT = 'task/uploadVideo'
const GET_VIDEO_LIST_ENDPOINT = 'task/getVideo'
const DEL_ENDPOINT = 'task/del'

const axiosInstance: AxiosInstance = axios.create({
  baseURL: BASE_URL,
  timeout: 10000, // 请求超时时间
  headers: {
    'Content-Type': 'application/json',
  },
});

// 添加请求拦截器
axiosInstance.interceptors.request.use(
  (config: InternalAxiosRequestConfig) => {
    // 在发送请求之前做些什么
    return config;
  },
  (error) => {
    // 对请求错误做些什么
    return Promise.reject(error);
  }
);

// 添加响应拦截器
axiosInstance.interceptors.response.use(
  (response: AxiosResponse) => {
    // 对响应数据做点什么
    return response.data; // 直接返回响应数据
  },
  (error) => {
    // 对响应错误做点什么
    if (error.response) {
      // 请求已发出，但服务器响应的状态码不在 2xx 范围内
      console.error('Response Error:', error.response.data);
    } else if (error.request) {
      // 请求已发出，但没有收到响应
      console.error('Network Error:', error.request);
    } else {
      // 发生了一些问题导致请求无法发出
      console.error('Error:', error.message);
    }
    return Promise.reject(error);
  }
);

// 定义一个获取数据的方法
// export const getData = async (endpoint: string, params?: any) => {
//   try {
//     const response = await axiosInstance.get(endpoint, { params });
//     return response;
//   } catch (error) {
//     throw error;
//   }
// };

// 你可以在这里添加更多的 API 方法
// 例如：
const postData = async (endpoint: string, data: any) => {
  try {
    const response = await axiosInstance.post(endpoint, data);
    return response;
  } catch (error) {
    throw error;
  }
};

export const getFieldRule = async () =>{
    return postData(GET_FIELD_RULE_ENDPOINT,'')
}

export const uploadImageURL = BASE_URL + '/' + UPLOAD_IMAGE_ENDPOINT

export const getImgList = async () =>{
  return postData(GET_IMAGE_LIST_ENDPOINT,'')
}

export const uploadVideoURL = BASE_URL + '/' + UPLOAD_VIDEO_ENDPOINT

export const getVideoList = async () =>{
  return postData(GET_VIDEO_LIST_ENDPOINT,'')
}

export const delThings = async (Url : string) =>{
  return postData(DEL_ENDPOINT, {
    url: Url
  })
}