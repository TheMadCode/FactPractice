<script setup>

    import Modal from './Modal.vue';

    const props = defineProps({
        showModal: {
            type: Boolean,
            required: true,
        },

        items: {
            required: true,
        },

        groups: {
            required: true,
        }
    })
</script>

<template>

<Teleport to="body">
  <!-- use the modal component, pass in the prop -->
  <Modal :show="showModal" >
    <template #header>
      <h3>Режим редактирования</h3>
    </template>
    <template #body>
        <div class="container-xs">
            <form onsubmit="alert('submit!');return false">
                <ul class="edit-list">
                    <li v-for="item in items" class="row edit-item">
                        <div class="col">
                            <input required id="name" v-model="item.name" type="text" @focusin="setCurrentField" @focusout="removeCurrentField" class="form-control" placeholder="Имя">
                        </div>

                        <div class="col">
                            <input required id="surname" v-model="item.surname" type="text" @focusin="setCurrentField"  @focusout="removeCurrentField" class="form-control" placeholder="Фамилия">
                        </div>

                        <div class="col">
                            <input required id="middle_name" v-model="item.middle_name" type="text" @focusin="setCurrentField" @focusout="removeCurrentField" class="form-control" placeholder="Отчество">
                        </div>

                        <div class="col">
                            <input required @keypress="isNumber($event)" id="average_mark" v-model="item.average_mark" type="text" @focusin="setCurrentField" @focusout="removeCurrentField" class="form-control" placeholder="Средняя оценка">
                        </div>


                        <div class="col">
                            <div class="col">
                                <Datepicker aria-required="true" :clearable="false" v-model="item.birth_date" :enable-time-picker="false" placeholder="Дата рождения" auto-apply></Datepicker>
                                <!-- <input v-model="" type="text" class="form-control" placeholder="Дата рождения"> -->
                            </div>
                            <!-- <input id="birthday" v-model="" type="text" @focusin="setCurrentField" @focusout="removeCurrentField" class="form-control" placeholder="Дата рождения"> -->
                        </div>

                        <div class="col">
                            <select required id="group" v-model="item.group" @focusin="setCurrentField" @focusout="removeCurrentField" class="form-control" placeholder="Группа">
                                <option v-for="item, value in groups" :value="value">{{ item }}</option>
                            </select>
                        </div>
                    </li>
                </ul>
            </form>
        </div>
    </template>
    <template #footer>
        <div class="container-xxl p-0">
            <div class="row p-0 d-flex justify-content-between">
                <div class="col-auto close_action">
                    <button @click="$emit('close')">
                    Закрыть</button>
                </div>
                <div class="col-auto main_action">
                    <button type="submit" @click="save">
                    Сохранить</button>
                </div>
            </div>
        </div>

    </template>
</Modal>
</Teleport>

</template>

<script>
    // console.log(groups)
    export default {
        emits: ['save', 'hideHint', 'showHint', 'close'],
        data() {
            return {
                // checker:  setInterval(() => {
                //     this.items.forEach(item => {
                //         item.target.name;
                //         item.target.surname;
                //         item.target.middle_name;
                //         item.target.average_mark;
                //         item.target.group;
                //         item.target.surname;
                //     });
                    
                // }, 100)
                // currentItems: [...this.items],
            }
        },

        methods: {
            save() {
                // console.log(this.groups)
                this.$emit('save', this.items);
            },

            isNumber: function(evt) {
                evt = (evt) ? evt : window.event;
                var charCode = (evt.which) ? evt.which : evt.keyCode;
                if (((charCode > 31 && (charCode < 48 || charCode > 57)) && charCode !== 46)) {
                    evt.preventDefault();
                } else {
                    if ((evt.target.value + evt.key > 5) || (evt.target.value + evt.key < 2)) {
                        evt.preventDefault();
                    }
                    return true;
            }},

            setCurrentField(event) {
                // console.log(this.items);
                var responseText = "";
                switch(event.target.attributes.id.value) {
                    case('name'):
                        responseText = "Имя";
                        break;

                    case('surname'):
                        responseText = "Фамилия";
                        break;

                    case('middle_name'):
                        responseText = "Отчество";
                        break;

                    case('average_mark'):
                        responseText = "Средняя оценка";
                        break;

                    case('group'):
                        responseText = "Группа";
                        break;

                    case('birthday'):
                        responseText = "Дата рождения";
                        break;
                }
                this.$emit("showHint", responseText);
            },

            removeCurrentField() {
                this.$emit("hideHint");
            },

            // change(event, type, uuid) {
            //     this.items.forEach(item => {
            //         console.log(item.target);
            //         if (item.uuid === uuid){
            //             item.name = event.target.value;
            //         }
            //     })

            //     console.log(this.items)

            //     console.log(uuid);
            //     console.log(event.target.value);
                
            // },

            close() {
                this.$emit('close');
            },

            getItemClassName() {
                return "body-item"
            }
        }
    }

</script>

<style>

    .form-control .table-input {
        width: 100%;
        height: 100%;
        border-radius: 0;
        padding: 0;
    }

    .edit-list {
        padding-left: 2%;
        padding-right: 2%;
        padding-top: 2%;
        max-height: 60vh;

        overflow-y: scroll;
        overflow-x: scroll;
    }

    .edit-item {
        min-width: fit-content;
        padding-bottom: 2%;
    }

    input.form-control {
        min-width: 100px;
        border-radius: 0px;
        border: 0;
        border-bottom: 1px ridge rgb(103, 103, 103);
        font-size: 12px;
        background-color: transparent;

    }

    input.form-control:focus { 
        outline: none;
        border-color: #dedede;
        box-shadow:  -1px -1px 6px #f2f2f2, 1px 1px 6px #D7E1F0
    }

    .modal-container {
        width: 1100px;
        margin: auto;
        padding: 20px 30px;
        background-color: #fff;
        border-radius: 2px;
        box-shadow: 0 2px 8px rgba(0, 0, 0, 0.33);
        transition: all 0.3s ease;
    }

</style>