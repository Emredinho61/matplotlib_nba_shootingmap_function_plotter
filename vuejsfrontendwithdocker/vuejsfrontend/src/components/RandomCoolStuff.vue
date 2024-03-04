<template>
    <Toast group="tl" />
    <div class="formgrid grid">
        <div class="field col">
            <Card>
                <template #title>NBA Plots</template>
                <template #content>
                    <Dialog v-model:visible="infovisible" modal header="Explanation" :style="{ width: '50vw' }">
                        Due to faulty data, I decided to remove the Seasons 2020-2022. The data is scaled differently.
                    </Dialog>
                    <div>
                        <Dropdown v-model="selectedSeason" :options="seasons" optionLabel="name"
                            placeholder="Select a Season" class="w-full md:w-14rem" />
                        <Button @click="postNBA" label="Submit Season"></Button>
                        <span><Button icon="pi pi-info-circle" class="p-button-rounded p-button-sm p-button-text"
                                @click="infovisible = true"></Button></span>
                    </div>
                    <div v-if="showRest" style="margin-top: 20px;">
                        <div class="card flex justify-content-center" style="margin-bottom: 20px">
                            <div class="flex flex-wrap gap-3" style="margin: 20px">
                                <div class="flex align-items-center">
                                    <RadioButton v-model="checkedHeatMap" inputId="Heatmap" name="heatmap" value="True" />
                                    <label for="Heatmap" class="ml-2">Heatmap</label>
                                </div>
                                <div class="flex align-items-center">
                                    <RadioButton v-model="checkedHeatMap" inputId="NormalPosition" name="position"
                                        value="False" />
                                    <label for="NormalPosition" class="ml-2">Position Shots</label>
                                </div>
                            </div>
                            <div class="flex flex-wrap gap-3">
                                <div class="flex align-items-center">
                                    <RadioButton v-model="checked" inputId="Made" name="made" value="False" />
                                    <label for="Made" class="ml-2">Made Shots</label>
                                </div>
                                <div class="flex align-items-center">
                                    <RadioButton v-model="checked" inputId="Missed" name="missed" value="True" />
                                    <label for="Missed" class="ml-2">Missed Shots</label>
                                </div>
                            </div>
                        </div>
                        <CascadeSelect v-model="selectedPlayer" :options="teams" optionLabel="pname"
                            optionGroupLabel="tname" :optionGroupChildren="['players']" style="min-width: 14rem"
                            placeholder="Select a Player" />
                        <Button @click="receiveNBAPlot" label="Submit Playerselection"></Button>
                    </div>
                </template>
            </Card>
        </div>
        <div class="field col">
            <Card>
                <template #title>NBA Shooting Map</template>
                <template #content>
                    <div class="card flex justify-content-center">
                        <Image v-if="imgData" :src="imgData" preview />
                    </div>
                </template>
            </Card>
        </div>
    </div>
</template>

<script>
import axios from "axios";

export default {
    data() {
        return {
            infovisible: false,
            checked: "False",
            checkedHeatMap: "False",
            imgData: null,
            showRest: false,
            selectedSeason: { name: 'Season 2004', code: 2004 },
            seasons: [
                { name: 'Season 2004', code: 2004 },
                { name: 'Season 2005', code: 2005 },
                { name: 'Season 2006', code: 2006 },
                { name: 'Season 2007', code: 2007 },
                { name: 'Season 2008', code: 2008 },
                { name: 'Season 2009', code: 2009 },
                { name: 'Season 2010', code: 2010 },
                { name: 'Season 2011', code: 2011 },
                { name: 'Season 2012', code: 2012 },
                { name: 'Season 2013', code: 2013 },
                { name: 'Season 2014', code: 2014 },
                { name: 'Season 2015', code: 2015 },
                { name: 'Season 2016', code: 2016 },
                { name: 'Season 2017', code: 2017 },
                { name: 'Season 2018', code: 2018 },
                { name: 'Season 2019', code: 2019 },
                { name: 'Season 2023', code: 2023 },
            ],
            selectedPlayer: null,
            teams: []
        }
    },
    methods: {
        receiveNBAPlot() {
            let playselection = { selectedPlayer: this.selectedPlayer, missed: this.checked, season: this.selectedSeason.code, heatmap: this.checkedHeatMap }
            axios.post("/api/postPlotNBA", playselection, {
                responseType: 'arraybuffer',
            }).then((response) => {
                const blob = new Blob([response.data], { type: 'image/png' });
                this.imgData = URL.createObjectURL(blob);
            }).catch((error) => {
                console.log(error);
                this.$toast.add({
                    severity: "error",
                    summary: "Error",
                    detail: "Dont forget to choose a Player!",
                    group: "tl",
                    life: 3000,
                });
            })
        },
        postNBA() {
            this.showRest = false;
            this.teams = []
            this.selectedPlayer = null;
            let trigData = {
                selectedSeason: this.selectedSeason
            }
            axios.post("/api/postNBA", trigData)
                .then((response) => {
                    this.teams = response.data;
                }).catch((error) => {
                    console.log(error);
                    this.$toast.add({
                        severity: "error",
                        summary: "Error",
                        detail: error.data,
                        group: "tl",
                        life: 3000,
                    });
                })
            this.showRest = true;

        }
    }
};

</script>   