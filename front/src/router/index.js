import {createRouter, createWebHistory} from 'vue-router'
import Main from "@/views/Main.vue";
import Login from "@/views/Login.vue";
import AboutView from "@/views/AboutView.vue";
import Host from "@/views/Host.vue";
import store from "@/store";

const routes = [
    {
        meta: {
            title: '自动化运维平台',
            requireAuth: true
        },
        path: '/main',
        name: 'main',
        component: Main,
        children: [
            {
                meta: {
                    title: '关于',
                    requireAuth: true
                },
                path: 'about',
                name: 'about',
                component: AboutView
            },
            {
                meta: {
                    title: '资产管理',
                    requireAuth: true
                },
                path: 'host',
                name: 'host',
                component: Host
            }

        ]
    },
    {
        meta: {
            title: '登录',
            requireAuth: false
        },
        path: '/login',
        alias: '/',
        name: 'login',
        component: Login

    }
]

const router = createRouter({
    history: createWebHistory(process.env.BASE_URL),
    routes
})

// 路由守卫
router.beforeEach((to, from, next) => {
    document.title = to.meta.title
    console.log(store.getters.token)
    if (to.meta.requireAuth &&  store.getters.token==="") {
               next('/login')
    }else {
        next()
    }
})

export default router

