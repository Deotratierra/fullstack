
class WorkersPage {

     // #####     INITIALIZATION     #####
    constructor() {
        // Init notifier
        this.notifier = new Notifier();

        // Inititialize all
        this._init_all();

        // Get workers
        this.getWorkers();
    }

    _init_all() {
        // Initialize Modals
        this._init_modals();

        // Initialize workers list
        this.workersList = new Vue( this._init_workersList() );
    }

    _init_modals() {
        // Add worker modal
        this.addWorkerModal = this._addWorkerModal();
        this._init_addWorkerModal();

        // Edit worker modal
        this.editWorkerModal = this._editWorkerModal();
        this._init_editWorkerModal();
    }

    // ==============================================

     // #####     MODALS     #####

    _addWorkerModal() {
        // Init modal
        const modal = $("#add-worker-modal");

        // Settings
        const settings = {
            inDuration: 500,
            outDuration: 200,
            startingTop: '50%',
            endingTop: '10%',
        }
        modal.modal(settings);

        // Input fields
        const inputs = {
            title: $("#add-worker-input-title"),
            address: $("#add-worker-input-address"),
            password: $("#add-worker-input-password")
        }

        // Buttons
        const buttons = {
            inside: {
                cancel: $("#add-worker-modal-cancel"),
                save: $("#add-worker-modal-save")
            },
            out: {
                open: $("#add-worker-modal-trigger")
            }
        }

        modal.settings = settings;
        modal.inputs = inputs;
        modal.buttons = buttons;
        return modal;
    }

    _init_addWorkerModal() {
        // Init modal buttons
        const modal = this.addWorkerModal;
        // Open button
        modal.buttons.out.open.click( () => {
            modal.modal("open");
        })
        // Cancel button
        modal.buttons.inside.cancel.click( () => {
            modal.modal("close");
        })
        // Save button
        modal.buttons.inside.save.click( () => {
            axios({
                method: "post",
                url: "/api/workers",
                params: {
                    title: modal.inputs.title.val(),
                    address: modal.inputs.address.val(),
                    password: modal.inputs.password.val()
                },
                xsrfCookieName: "_xsrf",
                xsrfHeaderName: "X-XSRFToken"
            }).then( (response) => {
                if (response.status == 200) {
                    this.notifier.successMsg(response.data, 4000);
                    this.getWorkers();
                } else {
                    this.notifier.errorMsg(response.data, 4000);
                }
            }).catch( (error) => {
                this.notifier.errorMsg("Error adding worker. Please, try again.",
                                       4000);
            })
            modal.modal("close");
        })
    }

    _editWorkerModal() {
        // Init modal
        const modal = $("#edit-worker-modal");

        // Settings
        const settings = {
            inDuration: 500,
            outDuration: 200,
            startingTop: '50%',
            endingTop: '10%',
        }
        modal.modal(settings);

        // Input fields
        const inputs = {
            title: $("#edit-worker-input-title"),
            address: $("#edit-worker-input-address"),
            password: $("#edit-worker-input-password")
        }

        // Buttons
        const buttons = {
            cancel: $("#edit-worker-modal-cancel"),
            save: $("#edit-worker-modal-save")
        }

        const methods = {
            open: () => { modal.modal("open") }
        }

        modal.settings = settings;
        modal.inputs = inputs;
        modal.buttons = buttons;
        modal.methods = methods;
        return modal;
    }

    _init_editWorkerModal() {
        // Init modal buttons
        const modal = this.editWorkerModal;
        // Cancel button
        modal.buttons.cancel.click( () => {
            modal.modal("close");
        })
        modal.buttons.save.click( () => {
            axios({
                method: "patch",
                url: "/api/workers",
                params: {
                    title: modal.inputs.title.val(),
                    address: modal.inputs.address.val(),
                    password: modal.inputs.password.val(),
                    _id: modal.temp_id
                },
                xsrfCookieName: "_xsrf",
                xsrfHeaderName: "X-XSRFToken"
            }).then( (response) => {
                if (response.status == 200) {
                    this.notifier.successMsg(response.data, 4000);
                    this.getWorkers();
                } else {
                    this.notifier.errorMsg(response.data, 4000);
                }
            }).catch( (error) => {
                this.notifier.errorMsg("Error editing worker. Please, try again.",
                                       4000);
            })
            modal.modal("close");
        })
    }

    // ==============================================

     // #####     LIST     #####

    _init_workersList() {
        return {
            delimiters: ["${", "}"], // Tornado Vue template conflict
            el: "#show-workers",
            data: {
                workers: []
            },
            methods: {
                del: (id) => {
                    console.log("DELETE WORKER", id)
                    axios({
                        method: "delete",
                        url: "/api/workers",
                        params: {
                            _id: id
                        },
                        xsrfCookieName: "_xsrf",
                        xsrfHeaderName: "X-XSRFToken"
                    }).then( (response) => {
                        if (response.status == 200){
                            this.notifier.successMsg(response.data, 3000);
                            this.getWorkers();
                        } else {

                            this.notifier.errorMsg(response.data, 3000);
                        }
                        console.log(response)

                    }).catch( (error) => {
                        this.notifier.errorMsg("Error removing worker. Please, try again.", 3000);
                    });
                },

                edit: (id, title, address, password) => {
                    this.editWorkerModal.inputs.title.val(title);
                    this.editWorkerModal.inputs.address.val(address);
                    this.editWorkerModal.inputs.password.val(password);
                    this.editWorkerModal.temp_id = id;
                    this.editWorkerModal.methods.open();
                    console.log("EDIT WORKER", id, title, address, password)
                }
            }
        }
    }

    // ==============================================

    // #####     ACTIONS     #####

    // Ask to server for workers
    getWorkers() {
        axios({
            method: "get",
            url: "/api/workers"
        }).then( (response) => {
            console.log(response);
            this.workersList.workers = response.data;
        }).catch( (error) => {
            console.log(error);
        });
    }

    // ==============================================

}

$(document).ready(function() {
    const page = new WorkersPage();
});