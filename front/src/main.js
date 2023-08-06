import { createApp } from 'vue'
import App from './App.vue'
import router from './router'
import Antd from 'ant-design-vue'
import 'ant-design-vue/dist/reset.css'
import store from './store'
import settings from "@/settings";

const app = createApp(App)
let echarts = require('echarts')

app.use(store).use(router).use(Antd).mount('#app')
app.config.globalProperties.$settings = settings
app.config.globalProperties.$echarts = echarts

// createApp(App).use(store).use(router).mount('#app')
