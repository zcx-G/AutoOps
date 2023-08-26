import {createStore} from 'vuex'
import createPersistedState from 'vuex-persistedstate'


export default createStore({
    state: {
        token: '',
        remember: true
    },
    plugins: [createPersistedState({ // setState,getState自动触发,防止刷新vuex清空，所以存到本地
        key: 'vuex',
        setState(key, state) {
            if (state.remember) {
                localStorage[key] = JSON.stringify(state)
            } else {
                sessionStorage[key] = JSON.stringify(state)
            }

        },
        getState(key, state) {
            if (localStorage[key]) {
                return JSON.parse(localStorage[key]);
            } else if (sessionStorage[key]) {
                return JSON.parse(sessionStorage[key]);
            } else {
                return state; // 或者返回一个默认的状态对象
            }
        }

    })],
    getters: {
        get_user_info(state, getters) {
            let data = state.token.split(".")
            return JSON.parse(atob(data[1]))
        },
        token(state, getters) {
            return state.token
        },
        remember(state, getters) {
            return state.remember
        }
    },
    mutations: {  // 类似methods
        setToken(state, token) {
            // 设置本地保存token
            state.token = token
        },
        setRemember(state, remember) {
            // 设置记住登陆状态
            // localStorage.removeItem('vuex');
            // sessionStorage.removeItem('vuex');
            state.remember = remember
        },
    },
    actions: {},
    modules: {}
})
