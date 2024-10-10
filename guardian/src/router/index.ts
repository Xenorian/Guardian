import { createRouter, createWebHistory } from 'vue-router'
import LoginView from '../views/LoginView.vue'
import MainView from '../views/MainView.vue'
import IntroView from '../views/main/IntroView.vue'

import RuleMainView from '../views/main/rule/MainView.vue'
import RuleView from '../views/main/rule/RuleView.vue'
import FieldView from '../views/main/rule/FieldView.vue'

import { getLoginCookies,removeLoginCookies } from '../utils/cookie'

const router = createRouter({
  history: createWebHistory(import.meta.env.BASE_URL),

  routes: [
    { path: '/', redirect: '/home/intro' },
    { path: '/home', 
      redirect: '/home/intro',
      component: MainView ,
      meta: { breadcrumbName: '首页' },
      children:[
      {
        path:'intro',
        component: IntroView,
        meta: { breadcrumbName: '简介' },
      },
      {
        path:'rule',
        redirect: '/home/rule/showField',
        component: RuleMainView,
        meta: { breadcrumbName: '监管领域' },
        children:[
        {
          path:'showField',
          component: RuleView,
        },
        {
          path:'field',
          component: FieldView,
          meta: { breadcrumbName: '领域规则' },
        }
        ]
      },
      ]
    },
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
