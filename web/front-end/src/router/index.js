import { createRouter, createWebHistory } from "vue-router";

const routes = [
    {
        path: "/",
        redirect: "/hotlist"
    },
    {
        path: "/hotlist",
        name: "Hotlist",
        meta: {
            title: "摸摸鱼"
        },
        component: () => import("../views/Momoyu.vue")
    }
]

const router = createRouter({
    history: createWebHistory(process.env.BASE_URL),
    routes
});

export default router;