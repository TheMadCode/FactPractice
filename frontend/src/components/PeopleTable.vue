<script setup >
    import IconEdit from "./icons/IconEdit.vue";
    import IconCreate from "./icons/IconCreate.vue";
    import IconDelete from "./icons/IconDelete.vue";
    import IconReload from "./icons/IconReload.vue";
    import IconSave from "./icons/IconSave.vue";
    
    import Modal from "./Modal.vue";

</script>

<style>
    #table-container {
        background-color: rgba(252, 252, 252, 0.861);
    }

    .table {
        --easy-table-body-even-row-background-color: rgba(237, 237, 237, 0.526);
        --easy-table-header-font-size: 15px;
        --easy-table-header-background-color:  rgba(225, 225, 225, 0.475);
        /* --easy-table-header-font-weight: bold; */

    }

    #button-list {
       border: 1px solid #e0e0e0;
       border-bottom: none;
    }

</style>

<template>

    <Hint :text="currentFieldName" :is-active="showEditHint" @close="showEditHint = false"/>

    <PeopleTableFilter
     class=""
     @set="setFilter"
     @clear="clearFilter"
     :groups="groups"
     :filter="filter"
    />

    <AddUserModal 
        :show-modal="showUserModal"
        :new-record="newRecord"
        :groups="groups"
        @close = "showUserModal = false"
        @create_elem="createElem"
        @clear_inputs="clearUserModal"
    />

    <EditUserModal 
        :show-modal="showEditModal"
        :items="editItems"
        :groups="groups"
        @showHint="showHint"
        @hideHint="hideHint"
        @save = "save_edit"
        @close = "showEditModal = false"
    />

    <div id="table-container" class="containet-xxl p-0 shadow">
        <div id="button-list" class="row m-0 ps-2 pt-1 pb-1 pe-2">
            <div class="d-flex align-items-end justify-content-between">
                <div class="d-flex">
                    <button id="show-modal" @click="showUserModal = true" class="btn m-1 border-0">
                        <IconCreate></IconCreate>
                    </button>

                    <button :disabled="itemsSelected.length <= 0" v-on:click="edit" class="btn m-1 border-0">
                        <IconEdit></IconEdit>
                    </button>

                    <button :disabled="itemsSelected.length <= 0" v-on:click="remove" class="btn m-1 border-0">
                        <IconDelete></IconDelete>
                    </button>
                </div>
                <div class="d-flex">
                    <button v-on:click="this.reload" class="m-1 btn">
                        <IconReload></IconReload>
                    </button>

                    <button :disabled="this.actions.length <= 0" v-on:click="save" class="btn m-1 border-0">
                        <IconSave></IconSave>
                    </button>
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

                alternating
                :filter-options="filterOptions"
                v-model:items-selected="itemsSelected"
                show-index
            >
        <template #item-birth_date="{ birth_date }">
            <div>{{ birth_date.toDateString() }}</div>
        </template>

        <template #item-group="{ group }">
            <div>{{ this.groups[group] }}</div>
        </template>
    
    </EasyDataTable>
        </div>
    </div>
</template>

<script>

    import { uuid } from "vue3-uuid";

    import axious from "axios";

    import AddUserModal from "./addUserModal.vue";
    import EditUserModal from "./editUserModal.vue";
    import Hint from "./Hint.vue";

    import PeopleTableFilter from "./PeopleTableFilter.vue";
    import { ref } from "vue";

    // import ref from "vue";

    const httpClient = axious.create();

    const filter = {
        "name": ref(null),
        "surname": ref(null),
        "middle_name": ref(null),
        "average_mark": ref(null),
        "group": ref(null),
        "date_range": ref(null),
    };
    
    httpClient.defaults.timeout = 500;

    var enum_Action = {
        "Remove": 0x01,
        "Create": 0x02,
        "Edit": 0x03,
    }

    export default {

    created() {
        // console.log(
        httpClient.get("http://localhost:5050/groups.api/get").then(response => {
            if (response.status === 200) {
                response.data.forEach(item => {
                    // console.log(item);

                    const key = item.unique_id;
                    // var data = {}

                    // data[key] = item.group_name,
                    this.groups[key] = item.group_name;
                    // console.log(this.groups);
                });
            }
        });

        httpClient.get("http://localhost:5050/human.api/get_human").then(response => {
            if (response.status === 200) {
                response.data.forEach(item => {
                    // console.log(item);
                    this.people.push({
                        "name": item.name,
                        "surname": item.surname,
                        "middle_name": item.middle_name,
                        "average_mark": item.average_mark,
                        "birth_date": new Date(item.birth_date),
                        "uuid": item.uuid,
                        "group": item.unique_group,
                        "study_year": item.study_year,
                    })
                })
                // this.people = response.data;
                // console.log(typeof(this.people[0].birth_date))
                this.isLoading = false;
            }
            this.isLoading = false;

        }).catch(error => {
            
            if (error.code === axious.AxiosError.ERR_INVALID_URL) {
                this.info = "Люди не найдены.";
                this.isLoading = false;
            }
            else if (error.code === axious.AxiosError.ERR_BAD_RESPONSE) {
                this.info = "Произошла серверная ошибка.";
                this.isLoading = false;
            }
            else {
                this.info = "Произошла ошибка";
                this.isLoading = false;
            }
        });
    },

    emits: 'switch',

    data() {
        return {
            groups: {},
            people: [],

            itemsSelected: [],
            filterOptions: [],

            showUserModal: false,
            showEditModal: false,
            showEditHint: false,

            currentFieldName: "",

            editItems: [],

            newRecord: {
                name: "",
                surname: "",
                middle_name: "",
                average_mark: "",
                date_of_birth: null,
                group: null,
            },

            actions: [],

            showModal: false,
            isLoading: true,

            headers: [
                { text: "Фамилия", value: "surname", sortable: true },
                { text: "Имя", value: "name", sortable: true },
                { text: "Отчество", value: "middle_name", sortable: true },
                { text: "Средний балл", value: "average_mark", sortable: true },
                { text: "Дата рождения", value: "birth_date"},
                { text: "Группа", value: "group", sortable: true},
                // { text}
            ],
        };
    },
    methods: {
        // showRow(item) {
        //     console.log(this.itemsSelected);
        //     // document.getElementById('row-clicked').innerHTML = JSON.stringify(item);
        // },

        return_group_text(group) {
            return this.groups.forEach(item => {
                if (item[group] !== undefined) {
                    // console.log(1);
                    alert(item[group]);
                    return item[group];
                }
            })

            // return this.groups[0][group]
        },

        clearUserModal() {
            this.newRecord = {
                name: "",
                surname: "",
                middle_name: "",
                average_mark: "",
                date_of_birth: null,
                group: null
            };
        },

        showHint(text) {
            // console.log(text)
            this.showEditHint = true;
            this.currentFieldName = text
        },

        hideHint() {
            this.showEditHint = false;
        },

        createElem() {
            this.showUserModal = false;
            const user_uuid = uuid.v4();

            const user_data = {
                "name": this.newRecord.name,
                "surname": this.newRecord.surname,
                "middle_name":this.newRecord.middle_name,
                "average_mark": this.newRecord.average_mark,
                "birth_date": this.newRecord.date_of_birth,
                "group": this.newRecord.group,
                "study_year": -1,
                "uuid": user_uuid,
                
            };

            this.people.push(user_data);

            this.actions.push({
                "action": enum_Action.Create,
                "entity": user_data,
            })
        },

        removeElement: function (array, index) {
            array.splice(index, 1);
        },

        remove(item) {
            const copiedItems = [...this.itemsSelected];

            copiedItems.forEach((item) => {
                let indx = this.people.findIndex((element) => element.uuid == item.uuid);

                if (indx >= 0) {

                    this.actions.push({
                        "action": enum_Action.Remove,
                        "item": this.people[indx].uuid
                    });

                    this.removeElement(this.people, indx)
                }
            });

            this.itemsSelected.splice(0);
        },
        
        setFilter() {
            this.filterOptions = [];

            if (filter.name.value !== null) {
                this.filterOptions.push({
                    field: "name",
                    comparison: "in",
                    criteria: filter.name.value,
            })};

            if (filter.surname.value !== null) {
                this.filterOptions.push({
                    field: "surname",
                    comparison: "in",
                    criteria: filter.surname.value,
            })};

            if (filter.middle_name.value !== null) {
                this.filterOptions.push({
                    field: "middle_name",
                    comparison: "in",
                    criteria: filter.middle_name.value,
            })};

            if (filter.average_mark.value !== null) {
                this.filterOptions.push({
                    field: "average_mark",
                    comparison: "=",
                    criteria: parseFloat(filter.average_mark.value),
            })};

            if (filter.group.value !== null) {
                this.filterOptions.push({
                    field: "group",
                    comparison: "=",
                    criteria: filter.group.value,
            })};

            if (filter.date_range.value !== null) {
                this.filterOptions.push({
                    field: "birth_date",
                    comparison: "between",
                    criteria: filter.date_range.value,
            })};
            
            // console.log(filter.name.value);
            // this.filterOptions = {}
        },

        clearFilter() {
            this.filterOptions = [];

            filter.name.value = null;
            filter.surname.value = null;
            filter.middle_name.value = null;
            filter.average_mark.value = null;
            filter.group.value = null;
            filter.date_range.value = null;
        },

        edit() {
            this.editItems = [];
            
            // console.log(this.itemsSelected);
            let copiedItems = [...this.itemsSelected];

            copiedItems.forEach((item) => {
                this.editItems.push({
                    "name": item.name,
                    "surname": item.surname,
                    "middle_name": item.middle_name,
                    "birth_date": item.birth_date,
                    "average_mark": item.average_mark,
                    "uuid": item.uuid,
                    "group": item.group,
                    "study_year": -1,
                });
            })

            this.showEditModal = true;
            // this.itemsSelected = [];
        },

        save_edit(editItems) {
            editItems.forEach((item) => {
                // console.log(item);
                let indx = this.people.findIndex((element) => element.uuid == item.uuid);

                if (indx >= 0) {
                    this.people[indx].name = item.name;
                    this.people[indx].surname = item.surname;
                    this.people[indx].middle_name = item.middle_name;
                    this.people[indx].average_mark = item.average_mark;
                    this.people[indx].birth_date = item.birth_date;
                    this.people[indx].group = item.group;
                    this.people[indx].study_year = -1;
                    // this.people[indx].birth_date = item.birth_date;
                    // this.people[indx].birth_date = item.birth_date;

                    this.actions.push({
                        "action": enum_Action.Edit,
                        "entity": this.people[indx],
                    })
                }
            });

            // console.log(this.itemsSelected === editItems);
            this.showEditModal = false;

            this.itemsSelected = [];
            // console.log(editItems);

            // this.items = editItems;
            this.editItems = []
        },

        save() {
            // console.log(this.actions);
            httpClient.post("http://localhost:5050/human.api/save_changes", this.actions).then(
                response => {
                    if (response.status === 200) {
                        info = "Изменения сохранены";
                    }
                }
            ).catch(
                err => {
                    if (err.code === 500) {
                        info = "Произошла серверная ошибка";
                    }
                }
            );
            this.actions.splice(0);
        },

        revert() {
            
        },

        reload(item) {
            this.isLoading = true;
            this.people = [];
            this.itemsSelected = [];
            this.actions.splice(0);
            this.loadPeople();
        },

        loadPeople() {
            httpClient.get("http://localhost:5050/groups.api/get").then(response => {
            if (response.status === 200) {
                response.data.forEach(item => {
                    // console.log(item);

                    const key = item.unique_id;
                    // var data = {}

                    // data[key] = item.group_name,
                    this.groups[key] = item.group_name;
                    // console.log(this.groups);
                });
            }
        });

            httpClient.get("http://localhost:5050/human.api/get_human").then(response => {
                if (response.status === 200) {
                    response.data.forEach(item => {
                        // console.log(item);
                            this.people.push({
                            "name": item.name,
                            "surname": item.surname,
                            "middle_name": item.middle_name,
                            "average_mark": item.average_mark,
                            "birth_date": new Date(item.birth_date),
                            "uuid": item.uuid,
                            "group": item.unique_group,
                            "study_year": item.study_year
                        })
                    })
                    // this.people = response.data;
                    // console.log(typeof(this.people[0].birth_date))
                    this.isLoading = false;
             }
             else {
                this.loading = false;
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
    components: { IconCreate, IconDelete, IconEdit, IconReload, Modal, AddUserModal, Hint }
}
</script>