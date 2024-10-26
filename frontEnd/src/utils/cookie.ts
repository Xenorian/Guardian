import Cookies from 'js-cookie'

const LOGIN_COOKIE_KEY = 'login_cookie'
const EXPIRE_DATE = 7

export function getLoginCookies() {
  return Cookies.get(LOGIN_COOKIE_KEY)
}

export function setLoginCookies(value:string) {
  return Cookies.set(LOGIN_COOKIE_KEY, value, { expires: EXPIRE_DATE })
}

export function removeLoginCookies() {
  return Cookies.remove(LOGIN_COOKIE_KEY)
}
