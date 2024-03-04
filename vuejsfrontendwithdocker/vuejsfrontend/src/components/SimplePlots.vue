<template>
    <Toast group="tl" />
    <div class="formgrid grid">
        <div class="field col">
            <Card>
                <template #title>Simple Plot</template>
                <template #content>
                    <Dialog v-model:visible="infovisible" modal header="Explanation" :style="{ width: '50vw' }">
                        The equation should be in a format such that it can be interpreted by python. And should be
                        dependent on x.
                        <br>
                        <br>
                        <b>Example:</b>
                        <Divider />
                        2*x+5
                        <Divider />
                        x**2
                        <Divider />
                        12/x
                    </Dialog>
                    <form @submit.prevent="postToTrigFun">
                        <div class="grid" style="margin: 20px;">
                            <div class="col-12">
                                <div class="p-inputgroup flex-1" style="margin: 20px;">
                                    <span class="p-inputgroup-addon">Function</span>
                                    <InputText v-model="fun" :use-grouping="false" />
                                    <span><Button icon="pi pi-info-circle"
                                            class="p-button-rounded p-button-sm p-button-text"
                                            @click="infovisible = true"></Button></span>
                                </div>
                            </div>
                            <div class="col-6">
                                <div class="p-inputgroup flex-1" style="margin: 20px;">
                                    <span class="p-inputgroup-addon">Start</span>
                                    <InputNumber placeholder="start" v-model="start" />
                                </div>
                            </div>
                            <div class="col-6">
                                <div class="p-inputgroup flex-1" style="margin: 20px;">
                                    <span class="p-inputgroup-addon">Stop</span>
                                    <InputNumber placeholder="stop" v-model="stop" />
                                </div>
                            </div>
                            <div class="col-4">
                                <div class="p-inputgroup flex-1" style="margin: 20px;">
                                    <span class="p-inputgroup-addon">x-Label</span>
                                    <InputText placeholder="xlabel" v-model="xlabel" />
                                </div>
                            </div>
                            <div class="col-4">
                                <div class="p-inputgroup flex-1" style="margin: 20px;">
                                    <span class="p-inputgroup-addon">y-Label</span>
                                    <InputText placeholder="ylabel" v-model="ylabel" />
                                </div>
                            </div>
                            <div class="col-4">
                                <div class="p-inputgroup flex-1" style="margin: 20px;">
                                    <span class="p-inputgroup-addon">title</span>
                                    <InputText placeholder="title" v-model="title" />
                                </div>
                            </div>
                        </div>
                        <Button @click="postToTrigFun" type="submit" label="Submit"></Button>
                    </form>
                </template>
            </Card>
        </div>
        <div class="field col">
            <Card>
                <template #title>Plot of Simple Plot</template>
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
            fun: "2**x+5",
            start: 0,
            stop: 10,
            xlabel: "foo",
            ylabel: "bar",
            title: "example Title",
            imgData: null,
            infovisible: false,
        }
    },
    methods: {
        postToTrigFun() {
            let trigData = {
                start: this.start,
                stop: this.stop,
                fun: this.fun,
                xlabel: this.xlabel,
                ylabel: this.ylabel,
                title: this.title
            }
            axios.post("/api/postSimplePlot", trigData, {
                responseType: 'arraybuffer',
            })
                .then((response) => {
                    const blob = new Blob([response.data], { type: 'image/png' });
                    this.imgData = URL.createObjectURL(blob);
                }).catch((error) => {
                    console.log(error);
                    this.$toast.add({
                        severity: "error",
                        summary: "Error",
                        detail: "Use a format for the equation such that it is suitable for python!",
                        group: "tl",
                        life: 3000,
                    });
                })
        }
    }
};

</script>   