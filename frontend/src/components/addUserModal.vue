<script setup>

    import Modal from './Modal.vue';

    const props = defineProps({
        showModal: {
            type: Boolean,
            required: true,
        },

        newRecord: {
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
      <h3>Добавить пользователя</h3>
    </template>
    <template #body>
        <div class="container-xs">
            <form>
                <div class="row">
                    <div class="col">
                        <input v-model="newRecord.name" type="text"  class="form-control" placeholder="Имя">
                    </div>

                    <div class="col">
                        <input v-model="newRecord.surname" type="text" class="form-control" placeholder="Фамилия">
                    </div>

                    <div class="col">
                        <input v-model="newRecord.middle_name" type="text" class="form-control" placeholder="Отчество">
                    </div>

                    <div class="col">
                        <input @keypress="isNumber($event)" v-model="newRecord.average_mark" type="text" class="form-control" placeholder="Средняя оценка">
                    </div>

                    <div class="col">
                        <Datepicker placeholder="Дата рождения" :clearable="false" v-model="newRecord.date_of_birth" :enable-time-picker="false" auto-apply></Datepicker>
                        <!-- <input v-model="" type="text" class="form-control" placeholder="Дата рождения"> -->
                    </div>

                    <div class="col">
                        <select id="group" v-model="newRecord.group" class="form-control" placeholder="Группа">
                            <option v-for="value, key in groups" :value="key">{{ value }}</option>
                        </select>
                    </div>
                </div>
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
                    <button :disabled="
                        newRecord.group === null 
                        || newRecord.name.length < 1
                        || newRecord.surname.length < 1
                        || newRecord.middle_name.length < 1
                        || newRecord.average_mark.length < 1
                        || newRecord.date_of_birth === null
                    " @click="save">

                    Добавить</button>
                    <button @click="$emit('clear_inputs')">
                    Очистить</button>
                </div>
            </div> 
        </div>
    </template>
</Modal>
</Teleport>

</template>

<script>

    import { ref } from 'vue';

    export default {
        
        emits: ['close', 'clear_inputs', 'create_elem'],

        methods: {
            save() {
                this.$emit('create_elem');
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
        },

        // data: {
        //     flow: ['month', 'year', 'calendar'],
        // }
        // data: {
            
        // }
    }

</script>

<style>

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