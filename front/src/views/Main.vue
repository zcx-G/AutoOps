<template>
  <a-layout style="min-height: 100vh">
    <a-layout-sider v-model:collapsed="collapsed" collapsible style="background-color: #000000">
      <div class="logo"
           style="font-style: italic;text-align: center;font-size: 30px;color:#fff;margin: 10px 0;background-color: #000000;line-height: 50px;font-family: 'Times New Roman'">
        <span>Auto Ops</span>
      </div>
      <div class="logo"/>
      <a-menu v-for="menu in menu_list" v-model:selectedKeys="selectedKeys" theme="dark" mode="inline" style="background-color: #000000">
        <a-menu-item v-if="menu.children.length===0" :key="menu.id">

          <router-link :to="menu.menu_url">
            <desktop-outlined/>
            <span> {{ menu.title }}</span>
          </router-link>
        </a-menu-item>

        <a-sub-menu v-else :key="menu.id">
          <template #title>
            <span>
              <user-outlined/>
              <span>{{ menu.title }}</span>
            </span>
          </template>
          <a-menu-item v-for="child_menu in menu.children" :key="child_menu.id">
            <router-link :to="child_menu.menu_url">{{ child_menu.title }}</router-link>
          </a-menu-item>
        </a-sub-menu>
      </a-menu>
    </a-layout-sider>
    <a-layout>
      <a-layout-header style="background: #000; padding: 0"/>
      <a-layout-content style="margin: 0 16px">
        <router-view></router-view>
      </a-layout-content>
      <a-layout-footer style="text-align: center">
        Ant Design ©2018 Created by Ant UED
      </a-layout-footer>
    </a-layout>
  </a-layout>
</template>
<script>
import {DesktopOutlined, FileOutlined, PieChartOutlined, TeamOutlined, UserOutlined} from '@ant-design/icons-vue';
import {defineComponent, ref} from 'vue';

export default defineComponent({
  components: {
    PieChartOutlined,
    DesktopOutlined,
    UserOutlined,
    TeamOutlined,
    FileOutlined,
  },

  created(){
    console.log("user_info----",this.$store.getters.get_user_info)
  },

  data() {
    return {
      collapsed: ref(false),
      selectedKeys: ref(['1']),
      menu_list: [
        {
          id: 1, icon: 'mail', title: '展示中心', tube: '', 'menu_url': '/main/show_center', children: []
        },
        {
          id: 2, icon: 'mail', title: '资产管理', 'menu_url': '/main/host', children: []
        },
        {
          "id": 3, icon: 'bold', title: '批量任务', tube: '', menu_url: '/main/workbench', children: [
            {id: 10, icon: 'mail', title: '执行任务', 'menu_url': '/main/multi_exec'},
            {id: 11, icon: 'mail', title: '命令管理', 'menu_url': '/main/template_manage'},
          ]
        },
        {
          id: 4, icon: 'highlight', title: '代码发布', tube: '', menu_url: '/main/workbench', children: [
            {id: 12, title: '应用管理', menu_url: '/main/release'},
            {id: 13, title: '发布申请', menu_url: '/main/release'}
          ]
        },
        {id: 5, icon: 'mail', title: '定时计划', tube: '', menu_url: '/main/workbench', children: []},
        {
          id: 6, icon: 'mail', title: '配置管理', tube: '', menu_url: '/main/workbench', children: [
            {id: 14, title: '环境管理', 'menu_url': '/main/environment'},
            {id: 15, title: '服务配置', 'menu_url': '/main/workbench'},
            {id: 16, title: '应用配置', 'menu_url': '/main/workbench'}
          ]
        },
        {id: 7, icon: 'mail', title: '监控预警', tube: '', 'menu_url': '/main/workbench', children: []},
        {
          id: 8, icon: 'mail', title: '报警', tube: '', 'menu_url': '/main/workbench', children: [
            {id: 17, title: '报警历史', 'menu_url': '/main/workbench'},
            {id: 18, title: '报警联系人', 'menu_url': '/main/workbench'},
            {id: 19, title: '报警联系组', 'menu_url': '/main/workbench'}
          ]
        },
        {
          id: 9, icon: 'mail', title: '用户管理', tube: '', menu_url: '/main/workbench', children: [
            {id: 20, title: '账户管理', tube: '', menu_url: '/main/workbench'},
            {id: 21, title: '角色管理', tube: '', menu_url: '/main/workbench'},
            {id: 22, title: '系统设置', tube: '', menu_url: '/main/workbench'}
          ]
        }
      ]
    };
  },

});
</script>
<style>
#components-layout-demo-side .logo {
  height: 32px;
  margin: 16px;
  background: rgba(255, 255, 255, 0.3);
}

.site-layout .site-layout-background {
  background: #fff;
}

[data-theme='dark'] .site-layout .site-layout-background {
  background: #141414;
}
</style>