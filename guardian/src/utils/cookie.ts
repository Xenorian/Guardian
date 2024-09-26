import Cookies from 'js-cookie'

const EXPIRE_DATE = 7

export function getCookies(key) {
  return Cookies.get(key)
}

export function setCookies(key, value) {
  return Cookies.set(key, value, EXPIRE_DATE)
}

export function removeCookies(key) {
  return Cookies.remove(key)
}
