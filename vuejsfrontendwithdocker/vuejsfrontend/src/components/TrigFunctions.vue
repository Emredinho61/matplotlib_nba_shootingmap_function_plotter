<template>
    <div class="formgrid grid">
        <div class="field col">
            <Card>
                <template #title>Trigonometric Functions</template>
                <template #content>
                    <div class="grid">
                        <div class="col-12">
                            <div class="p-inputgroup flex-1" style="margin: 20px;">
                                <span class="p-inputgroup-addon">title</span>
                                <InputText placeholder="title" v-model="title" />
                            </div>
                        </div>
                    </div>
                    <div class="card flex justify-content-center" style="margin-bottom: 30px;">
                        <div class="flex flex-wrap gap-3">
                            <div class="flex align-items-center">
                                <RadioButton v-model="mode" inputId="sine" name="trig" value="sin" />
                                <label for="sine" class="ml-2">Sine</label>
                            </div>
                            <div class="flex align-items-center">
                                <RadioButton v-model="mode" inputId="cosine" name="trig" value="cos" />
                                <label for="cosine" class="ml-2">Cosine</label>
                            </div>
                            <div class="flex align-items-center">
                                <RadioButton v-model="mode" inputId="tangent" name="trig" value="tan" />
                                <label for="tangent" class="ml-2">Tangent</label>
                            </div>
                        </div>
                    </div>
                    <div class="grid">
                        <div class="col-6">
                            <div class="p-inputgroup flex-1">
                                <span class="p-inputgroup-addon">Start</span>
                                <InputNumber v-model="start" :use-grouping="false" placeholder="start" />
                            </div>
                        </div>
                        <div class="col-6">
                            <div class="p-inputgroup flex-1">
                                <span class="p-inputgroup-addon">Stop</span>
                                <InputNumber placeholder="stop" v-model="stop" />
                            </div>
                        </div>
                    </div>

                    <div class="grid" style="margin-top: 20px;">
                        <div class="col-3">
                            <div class="p-inputgroup flex-1">
                                <span class="p-inputgroup-addon">a</span>
                                <InputNumber v-model="a" :use-grouping="false" :placeholder="1" />
                            </div>
                        </div>
                        <div class="col-3">
                            <div class="p-inputgroup flex-1">
                                <span class="p-inputgroup-addon">b</span>
                                <InputNumber placeholder="1" v-model="b" />
                            </div>
                        </div>
                        <div class="col-3">
                            <div class="p-inputgroup flex-1">
                                <span class="p-inputgroup-addon">c</span>
                                <InputNumber placeholder="1" v-model="c" />
                            </div>
                        </div>
                        <div class="col-3">
                            <div class="p-inputgroup flex-1">
                                <span class="p-inputgroup-addon">d</span>
                                <InputNumber placeholder="1" v-model="d" />
                            </div>
                        </div>
                    </div>
                    <Button @click="postToTrigFun" label="Submit" style="margin-top: 20px;"></Button>
                </template>
            </Card>
        </div>
        <div class="field col">
            <Card>
                <template #title>Plot of Trigonometric Functions</template>
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
            mode: 'sin',
            start: 0,
            stop: 10,
            a: 1,
            b: 1,
            c: 1,
            d: 1,
            title: "Example Title",
            imgData: null
        }
    },
    methods: {
        postToTrigFun() {
            let trigData = {
                mode: this.mode,
                start: this.start,
                stop: this.stop,
                a: this.a,
                b: this.b,
                c: this.c,
                d: this.d,
                title: this.title
            }
            axios.post("/api/postTrig", trigData, {
                responseType: 'arraybuffer',
            }).then((response) => {
                const blob = new Blob([response.data], { type: 'image/png' });
                this.imgData = URL.createObjectURL(blob);
            }).catch((error) => {
                console.log(error);
            })
        }
    }
};

</script>   