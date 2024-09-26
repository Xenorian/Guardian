import { createRouter, createWebHistory } from 'vue-router'
import LoginView from '../views/LoginView.vue'
import MainView from '../views/MainView.vue'
import { getLoginCookies,removeLoginCookies } from '../utils/cookie'

const router = createRouter({
  history: createWebHistory(import.meta.env.BASE_URL),

  routes: [
    { path: '/', redirect: '/home' },
    { path: '/home', component: MainView },
    { path: '/login', component: LoginView },
  ],
})

// 全局前置守卫
router.beforeEach((to, from, next) => {
  const hasCookie = getLoginCookies(); // 检查是否有特定的 cookie

  // 如果目标路由是登录页，且有 cookie，则重定向到首页
  if (to.path === '/login' && hasCookie) {
    // next({ path: '/home' });
    removeLoginCookies()
    next();
  } 
  // 如果没有 cookie，且目标路由不是登录页，则重定向到登录页
  else if (!hasCookie && to.path !== '/login') {
    next({ path: '/login' });
  } 
  // 其他情况，继续导航
  else {
    next();
  }
});

export default router
