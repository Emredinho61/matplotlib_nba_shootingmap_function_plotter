<template>
    <div class="card" v-if="mode">
        <div class="flex mb-2 gap-2 justify-content-end">
            <Button @click="active = 0" rounded label="1" class="w-2rem h-2rem p-0" :outlined="active !== 0" />
            <Button @click="active = 1" rounded label="2" class="w-2rem h-2rem p-0" :outlined="active !== 1" />
            <Button @click="active = 2" rounded label="3" class="w-2rem h-2rem p-0" :outlined="active !== 2" />
            <Button @click="active = 3" rounded label="4" class="w-2rem h-2rem p-0" :outlined="active !== 3" />
            <Button @click="active = 4" rounded label="5" class="w-2rem h-2rem p-0" :outlined="active !== 4" />
        </div>
        <TabMenu v-model:activeIndex="active" :model="items" />
        <RandomCoolStuff v-if="active === 0"></RandomCoolStuff>
        <SimplePlots v-if="active === 1"></SimplePlots>
        <BarChart v-if="active === 2"></BarChart>
        <PieChart v-if="active === 3"></PieChart>
        <TrigFunctions v-if="active === 4"></TrigFunctions>
    </div>
    <div v-else>


    </div>
</template>
<script>
import BarChart from '@/components/BarChart.vue'
import PieChart from '@/components/PieChart.vue'
import SimplePlots from '@/components/SimplePlots.vue'
import TrigFunctions from '@/components/TrigFunctions.vue'
import RandomCoolStuff from '@/components/RandomCoolStuff.vue'

export default {
    data() {
        return {
            active: 0,
            items: [
                { label: 'NBA Shooting Heatmap', icon: 'pi pi-globe' },
                { label: 'Simple Plots', icon: 'pi pi-chart-line' },
                { label: 'Bar Chart', icon: 'pi pi-chart-bar' },
                { label: 'Pie Chart', icon: 'pi pi-chart-pie' },
                { label: 'Trigonometric Functions', icon: 'pi pi-image' },
            ],
            mode: true
        }
    },
    components: {
        BarChart,
        PieChart,
        SimplePlots,
        TrigFunctions,
        RandomCoolStuff
    }
}

</script>