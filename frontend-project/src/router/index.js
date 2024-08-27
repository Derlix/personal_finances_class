//Aqui solo van las rutas del front end
import { createRouter, createWebHistory } from 'vue-router';
import LoginView from '../views/LoginView.vue';
import FortgotPassView from '../views/FortgotPassView.vue';
import NotFoundView from '../views/NotFoundView.vue'
const routes = [
 // Ruta por defecto que apunta a LoginView
 { path: '/', name: 'Login', component: LoginView },
 // Otras rutas
 { path: '/forgot-password', name: 'ForgotPass', component:FortgotPassView },
 {path: '/not-found', name:'NotFound', component:NotFoundView},
 // Redirección en caso de ruta no encontrada
 { path: '/:pathMatch(.*)*', redirect: '/not-found' },
];


const router = createRouter({
 history: createWebHistory(process.env.VITE_BASE_URL),
 routes,
});
export default router;
