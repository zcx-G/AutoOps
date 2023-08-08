import {createRouter, createWebHistory} from 'vue-router'
import Main from "@/views/Main.vue";
import Login from "@/views/Login.vue";
import AboutView from "@/views/AboutView.vue";
import Host from "@/views/Host.vue";

const routes = [
    {
        meta: {
            title: '自动化运维平台'
        },
        path: '/main',
        name: 'main',
        component: Main,
        children: [
            {
                path: 'about',
                name: 'about',
                component: AboutView
            },
            {
                path: 'host',
                name: 'host',
                component: Host
            }

        ]
    },
    {
        meta: {
            title: '登录'
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

export default router
