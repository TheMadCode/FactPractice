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
                        <input type="text" class="form-control" placeholder="Имя">
                    </div>

                    <div class="col">
                        <input type="text" class="form-control" placeholder="Фамилия">
                    </div>

                    <div class="col">
                        <input type="text" class="form-control" placeholder="Отчество">
                    </div>

                    <div class="col">
                        <input type="text" class="form-control" placeholder="Средняя оценка">
                    </div>

                    <div class="col">
                        <select id="group" type="text" class="form-control" placeholder="Группа">
                            <option v-for="value, key in groups" :value="key">{{ value }}</option>
                        </select>
                    </div>

                    <div class="col">
                        <Datepicker :enable-time-picker="false" auto-apply></Datepicker>
                        <!-- <input v-model="" type="text" class="form-control" placeholder="Дата рождения"> -->
                    </div>
                </div>

                <div class="row m-0 pt-1 pb-4">
                    <div class="d-flex align-items-end justify-content-start">
                        <button>Применить</button>
                        <button>Очистить</button>
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
    }
})

</script>