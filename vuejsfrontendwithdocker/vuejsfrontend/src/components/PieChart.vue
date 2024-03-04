<template>
    <Toast group="tl" />
    <div class="formgrid grid">
        <div class="field col">
            <Card>
                <template #title>Pie Chart</template>
                <template #content>
                    <div class="grid">
                        <div class="col-12">
                            <div class="p-inputgroup flex-1" style="margin: 20px;">
                                <span class="p-inputgroup-addon">title</span>
                                <InputText placeholder="title" v-model="title" />
                            </div>
                        </div>
                    </div>
                    <div class="formgrid grid">
                        <Button label="Add Row" @click="addNewColumn" style="margin: 20px;"></Button>
                        <Button label="Remove Row" @click="removeColumn" style="margin: 20px;"></Button>
                    </div>

                    <div class="card p-fluid">
                        <DataTable v-model:editingRows="editingRows" :value="values" editMode="row" dataKey="id"
                            @row-edit-save="onRowEditSave" :pt="{
                                table: { style: 'min-width: 50rem' },
                                column: {
                                    bodycell: ({ state }) => ({
                                        style: state['d_editing'] && 'padding-top: 0.6rem; padding-bottom: 0.6rem',
                                    }),
                                },
                            }">
                            <Column field="id" header="ID" style="width: 20%" :editable="false"></Column>
                            <Column field="name" header="Name" style="width: 40%">
                                <template #editor="{ data, field }">
                                    <InputText v-model="data[field]" />
                                </template>
                            </Column>
                            <Column field="val" header="Value" style="width: 40%">
                                <template #editor="{ data, field }">
                                    <InputNumber v-model="data[field]" :max-fraction-digits="2" :min="0" :max="100"/>
                                </template>
                            </Column>
                            <Column field="color" header="Color" :editable="true">
                                <template #editor="{ data, field }">
                                    <ColorPicker v-model="data[field]" />
                                </template>
                            </Column>
                            <Column :rowEditor="true" style="width: 10%; min-width: 8rem" bodyStyle="text-align:center">
                            </Column>
                        </DataTable>
                    </div>
                    <Button @click="postBarChart" label="Submit" style="margin-top: 20px;"></Button>
                </template>
            </Card>
        </div>
        <div class="field col">
            <Card>
                <template #title>Plot of Pie Chart</template>
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
            id: 1,
            values: [
                { id: 1, name: "Name 1", val: 0.0, color: "f02840" },
            ],
            editingRows: [],
            imgData: null,
            title: "Example Title"
        }
    },
    methods: {
        postBarChart() {
            if (this.totalValue() === 100) {
                let trigData = {
                    id: this.id,
                    values: this.values,
                    title: this.title
                }
                axios.post("/api/postPie", trigData, {
                    responseType: 'arraybuffer',
                }).then((response) => {
                    const blob = new Blob([response.data], { type: 'image/png' });
                    this.imgData = URL.createObjectURL(blob);
                    console.log(response);
                }).catch((error) => {
                    console.log(error);
                })
            } else {
                this.$toast.add({
                    severity: "error",
                    summary: "Error",
                    detail: "The Sum must add up to 100!",
                    group: "tl",
                    life: 3000,
                });
            }
        },
        onRowEditSave(event) {
            let { newData, index } = event;
            this.values[index] = newData;
        },
        addNewColumn() {
            this.id += 1;
            this.values.push({ id: this.id, name: 'New' + this.id, val: 0, color: 'f02840' })
        },
        removeColumn() {
            if (this.id >= 1) {
                this.values.pop();
                this.id -= 1;
            }
        },
        totalValue() {
            let sum = 0;
            for (let i = 0; i < this.values.length; i++) {
                sum += parseFloat(this.values[i].val);
            }
            return sum;
        },
    }
};

</script>   