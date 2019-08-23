import Vue from 'vue';
import App from './Example.vue';

Vue.config.productionTip = false;

const elSelector = '#example';
const mountEl = document.querySelector(elSelector);

new Vue({
    render: (h) => {
        const context = {
            props: { ...mountEl.dataset },
        };
        return h(App, context);
    },
}).$mount(elSelector);
