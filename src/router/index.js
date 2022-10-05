import Vue from 'vue'
import VueRouter from 'vue-router'
import LoginEs from '../components/LoginEs.vue'
import Dashboard from '../views/Dashboard.vue';

Vue.use(VueRouter)

const routes =[
    {
        path: '/',
        name: 'LoginEs',
        component: LoginEs
    },
    {
        path: '/dashboard',
        name: 'Dashboard',
        component: Dashboard
    }
]