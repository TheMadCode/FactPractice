<script setup>

    import IconInfo from "./icons/IconInfo.vue"

    const prop = defineProps({
        text: {
            type: String,
            required: true
        },

        isActive: {
            type: Boolean,
            required: true
        }
    })

</script>

<template>
    <Transition name="modal">
        <div v-show="isActive" class="hint-container">
            <IconInfo class="icon-color"></IconInfo>
            <div class="hint-text text-break">Вы изменяете поле '{{ text }}'</div>
            <div class="close-button-holder"><a @click="$emit('close')" class="close-button">Закрыть</a></div>
        </div>
    </Transition>
</template>

<style>
    .hint-container {
        z-index: 9999;
        position: fixed;
        right: 40px;
        bottom: 40px;

        max-width: 200px;
        min-width: 200px;

        background-color: rgb(255, 255, 255);
        box-shadow: 4px 4px 8px 0.5px  rgba(0, 0, 0, 0.278);
        color: rgb(30, 30, 30);
        text-align: center;

        transition: all 0.3s ease;
    }

    .hint-text {
        padding-top: 5px;
        padding-right: 10px;
        padding-left: 10px;
        margin: 0;
        max-width: 200px;
        font-size: large;
        font-weight: 600;
    }

    .close-button-holder {
        padding-bottom: 5px;
    }

    .close-button {
        color: rgb(5, 172, 102);
        margin-bottom: 5px;
    }

    .close-button:hover {
        color: rgb(216, 69, 11);
        background-color: transparent;
        margin-bottom: 5px;
    }

    .icon-color {
        padding-top: 2px;
        color: rgba(4, 138, 216, 0.806);
    }

    .hint-enter-from {
        opacity: 0;
    }

    .hint-leave-to {
        opacity: 0;
    }

    .hint-enter-from .hint-container,
    .hint-leave-to .hint-container {
        -webkit-transform: scale(1.1);
            transform: scale(1.1);
    }

</style>