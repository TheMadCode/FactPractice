<script setup>

    import Modal from './Modal.vue';

    const props = defineProps({
        showModal: {
            type: Boolean,
            required: true,
        },

        newRecord: {
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
                        <input v-model="newRecord.average_mark" type="text" class="form-control" placeholder="Средняя оценка">
                    </div>

                    <div class="col">
                        <input v-model="newRecord.date_of_birth" type="text" class="form-control" placeholder="Дата рождения">
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
                    <button @click="save">
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

    export default {
        emits: ['close', 'clear_inputs', 'create_elem'],
        
        methods: {
            save() {
                this.$emit('create_elem');
            }
        }
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