import ContentsTab from "../components/ContentsTab.vue"
import Menu from "../components/Menu.vue";
import RegisterCompetition from "../components/RegisterCompetition.vue";
import Vue from "vue"
import VueRouter from "vue-router"

Vue.use(VueRouter);

const routes = [
    { path: "/", component: Menu },
    {
        path: "/dashboard/:competition_id",
        name: "dashboard",
        component: ContentsTab
    },
    {
        path: "/register_competition/",
        name: "register_competition",
        component: RegisterCompetition
    }
];

const router = new VueRouter({
    routes
});

export default router;