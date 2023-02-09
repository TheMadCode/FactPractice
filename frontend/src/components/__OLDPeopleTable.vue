<template>

    <h4 class="text-danger">
        {{ info }}
    </h4>

    <div class="container-xxl">
        <div class="row">
            <table id="peopleTable" class="table">
                <thead>
                    <tr>
                        <th id="header" scope="col" v-for="header in headers">
                            {{ header }}
                        </th>
                        <!-- <th scope="col">Фамилия</th>
                        <th scope="col">Имя</th>
                        <th scope="col">Отчество</th>
                        <th scope="col">Средниц балл</th>
                        <th scope="col">Дата рождения</th> -->
                    </tr>
                </thead>
                <tbody>
                    <tr v-for = "person in people">
                        <th scope="col">{{ person.surname }}</th>
                        <th scope="col">{{ person.name }}</th>
                        <th scope="col">{{ person.middle_name }}</th>
                        <th scope="col">{{ person.birth_date }}</th>
                        <th scope="col">{{ person.average_mark }}</th>
                    </tr>

                    <!-- <tr>
                        <th scope="row">2</th>
                        <th scope="col">Котов</th>
                        <th scope="col">Игорь</th>
                        <th scope="col">Янович</th>
                        <th scope="col">4.2</th>
                        <th scope="col">18.10.2000</th>
                    </tr> -->
                    <!-- <tr>
                        <th scope="row">3</th>
                        <th scope="col">Котов</th>
                        <th scope="col">Игорь</th>
                        <th scope="col">Янович</th>
                        <th scope="col">4.2</th>
                        <th scope="col">18.10.2000</th>
                    </tr> -->
                    <!-- <tr>
                        <th scope="row">4</th>
                        <th scope="col">Котов</th>
                        <th scope="col">Игорь</th>
                        <th scope="col">Янович</th>
                        <th scope="col">4.2</th>
                        <th scope="col">18.10.2000</th>
                    </tr> -->
                </tbody>
            </table>
        </div>
    </div>
</template>

<script>

import axious from "axios";

const httpClient = axious.create();

httpClient.defaults.timeout = 500;

export default {

  data() {
    return {
        info: "",
        people: [],
        headers: [
            "Фамилия",
            "Имя",
            "Отчество",
            "Дата рождения",
            "Средняя оценка",
        ],
    }
  },

  mounted() {
    // console.log(
    httpClient.get(
        "http://localhost:5050/human.api/get_human"

    ).then(response => {
        if (response.status === 200){
            this.people = response.data;
        }

    }).catch(error => {
        if (error.code === axious.AxiosError.ERR_INVALID_URL) {
                this.info = "Люди не найдены."
            }

            else if (error.code === axious.AxiosError.ERR_BAD_RESPONSE) {
                this.info = "Произошла серверная ошибка."
            }

            else {
                this.info = "Произошла ошибка"
            }
    });
    }
}

</script>

<style>

    #header:hover {
        background-color: rgba(175, 175, 175, 0.150);
    }
    
</style>

/* 
<!-- <style>
th::root.dark-theme{
    color: rgb(240, 240, 240);
}
</style> --> */