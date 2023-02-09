<script setup >
    import IconEdit from "./icons/IconEdit.vue";
    import IconCreate from "./icons/IconCreate.vue";
    import IconDelete from "./icons/IconDelete.vue";
    import IconReload from "./icons/IconReload.vue";
    import IconSave from "./icons/IconSave.vue";

</script>

<style>
    #table-container {
        background-color: rgba(252, 252, 252, 0.861);
    }

    .table {
        --easy-table-body-even-row-background-color: rgba(228, 228, 228, 0.526);
        --easy-table-header-font-size: 15px;
        --easy-table-header-background-color:  rgba(194, 194, 194, 0.475);
        /* --easy-table-header-font-weight: bold; */

    }

    #button-list {
       border: 1px solid #e0e0e0;
       border-bottom: none;
    }

</style>

<template>
    <div id="table-container" class="containet-xxl p-0 shadow">
        <div id="button-list" class="row m-0 ps-2 pt-1 pb-1 pe-2">
            <div class="d-flex align-items-end justify-content-between">
                <div class="d-flex">
                    <div v-on:click="create" class="btn">
                        <IconCreate></IconCreate>
                    </div>

                    <div v-on:click="edit" class="btn">
                        <IconEdit></IconEdit>
                    </div>

                    <div v-on:click="remove" class="btn">
                        <IconDelete></IconDelete>
                    </div>
                </div>
                <div class="d-flex">
                    <div v-on:click="this.reload" class="btn">
                        <IconReload></IconReload>
                    </div>

                    <div v-on:click="save" class="btn">
                        <IconSave></IconSave>
                    </div>
                </div>
            </div>
        </div>
        <div class="row m-0 table">
            <EasyDataTable class="p-0"
                :headers="headers"
                :items="people"
                :loading="isLoading"
                border-cell
                buttons-pagination

                v-model:items-selected="itemsSelected"
                show-index

                @click-row="showRow"
            />
        </div>
    </div>
</template>

<script>

    import axious from "axios";

    const httpClient = axious.create();
    
    httpClient.defaults.timeout = 500;

    export default {
    mounted() {
        // console.log(
        httpClient.get("http://localhost:5050/human.api/get_human").then(response => {
            if (response.status === 200) {
                this.people = response.data;
                this.isLoading = false;
            }
        }).catch(error => {
            if (error.code === axious.AxiosError.ERR_INVALID_URL) {
                this.info = "Люди не найдены.";
            }
            else if (error.code === axious.AxiosError.ERR_BAD_RESPONSE) {
                this.info = "Произошла серверная ошибка.";
            }
            else {
                this.info = "Произошла ошибка";
            }
        });
    },
    data() {
        return {
            people: [],
            itemsSelected: [],
            opened: false,
            visible: false,
            isLoading: true,
            headers: [
                { text: "Фамилия", value: "surname", sortable: true },
                { text: "Имя", value: "name", sortable: true },
                { text: "Отчество", value: "middle_name", sortable: true },
                { text: "Средний балл", value: "average_mark", sortable: true },
                { text: "Дата рождения", value: "birth_date"},
            ],
        };
    },
    methods: {
        showRow(item) {
            console.log(this.itemsSelected);
            // document.getElementById('row-clicked').innerHTML = JSON.stringify(item);
        },

        create(item) {

        },

        removeElement: function (array, index) {
            array.splice(index, 1);
        },

        remove(item) {
            let copiedItems = [...this.itemsSelected];

            copiedItems.forEach((item) => {
                let indx = this.people.findIndex((element) => element.uuid == item.uuid);
                if (indx >= 0) {
                    this.removeElement(this.people, indx)
                }
            });
        },
        

        edit(item) {

        },

        save() {

        },

        revert() {
            
        },

        reload(item) {
            this.isLoading = true;
            this.people = [];
            this.itemsSelected = [];
            this.loadPeople();
        },

        confirm() {

        },

        cancel() {

        },

        loadPeople() {
            httpClient.get("http://localhost:5050/human.api/get_human").then(response => {
            if (response.status === 200) {
                this.people = response.data;
                this.isLoading = false;
            }
        }).catch(error => {
            if (error.code === axious.AxiosError.ERR_INVALID_URL) {
                this.info = "Люди не найдены.";
            }
            else if (error.code === axious.AxiosError.ERR_BAD_RESPONSE) {
                this.info = "Произошла серверная ошибка.";
            }
            else {
                this.info = "Произошла ошибка";
            }
        });
        }
    },
    components: { IconCreate, IconDelete, IconEdit, IconReload  }
}
</script>