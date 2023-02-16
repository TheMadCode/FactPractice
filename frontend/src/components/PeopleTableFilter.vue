<style>
    .filter-holder {
       border: 1px solid #e0e0e0;
       border-bottom: none;
    }
</style>

<template>
    <div class="containet-xxl filter-holder p-0 shadow">
        <div class="row m-0 ps-2 pt-1 pb-1 pe-2">
            <div class="d-flex align-items-end justify-content-between">          
                <h4 class="pt-3">Фильтр</h4>    
            </div>
            <hr class="w-100 mt-1 mb-3"/>
        </div>
        <div class="row m-0 table">
            <div class="container-xxl ps-4 pe-4 pt-2 pb-1 table-container">
                <div class="row m-0 pb-2 d-flex">
                    <div class="col">
                        <input v-model="filter.name.value" type="text" class="form-control" placeholder="Имя">
                    </div>

                    <div class="col">
                        <input v-model="filter.surname.value" type="text" class="form-control" placeholder="Фамилия">
                    </div>

                    <div class="col">
                        <input v-model="filter.middle_name.value" type="text" class="form-control" placeholder="Отчество">
                    </div>

                    <div class="col">
                        <input @keypress="isNumber($event)" v-model="filter.average_mark.value" type="text" class="form-control" placeholder="Средняя оценка">
                    </div>

                    <div class="col">
                        <Datepicker v-model="filter.date_range.value" placeholder="Даты рождения" :enable-time-picker="false" range auto-apply></Datepicker>
                    </div>

                    <div class="col">
                        <select v-model="filter.group.value" id="group" type="text" class="form-control" placeholder="Группа">
                            <option v-for="value, key in groups" :value="key">{{ value }}</option>
                        </select>
                    </div>
                </div>

                <div class="row m-0 pt-1 pb-4">
                    <div class="d-flex align-items-end justify-content-start">
                        <button :disabled = "(filter.name.value === null || filter.name.value === '')
                            && (filter.surname.value === null || filter.surname.value === '')
                            && (filter.middle_name.value === null || filter.middle_name.value === '')
                            && (filter.average_mark.value === null || filter.average_mark.value === '')
                            && filter.group.value === null
                            && filter.date_range.value === null" @click="set" >Применить</button>
                        <button @click="clear">Очистить</button>
                    </div>
                </div>
            </div>
        </div>
    </div>
</template>

<script setup>

    const props = defineProps({
        groups: {
            reqired: true,
        },

        filter: {
            required: true,
        }

    });

</script>

<script>

    export default {
        methods: {
            set() {
                this.$emit("set");
            },

            clear() {
                this.$emit("clear");
            },

            isNumber: function(evt) {
                evt = (evt) ? evt : window.event;
                var charCode = (evt.which) ? evt.which : evt.keyCode;
                if ((charCode > 31 && (charCode < 48 || charCode > 57)) && charCode !== 46) {
                    evt.preventDefault();;
                } else {
                    return true;
            }
    }
        }
        
    }

</script>