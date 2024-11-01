import { Component, inject } from "@angular/core";
import { ReactiveFormsModule, FormBuilder, Validators } from "@angular/forms";

@Component({
    selector: "app-register",
    templateUrl: "./register.component.html",
    standalone: true,
    imports: [ReactiveFormsModule],
})
export class RegisterComponent {
    fb = inject(FormBuilder);

    form = this.fb.nonNullable.group({
        username: ["", Validators.required],
        email: ["", Validators.required],
        password: ["", Validators.required]
    });

    onSubmit(): void {
        console.log("register");
    }
}