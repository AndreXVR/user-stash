import { Component, inject } from "@angular/core";
import { ReactiveFormsModule, FormBuilder, Validators } from "@angular/forms";

@Component({
    selector: "app-login",
    templateUrl: "./login.component.html",
    standalone: true,
    imports: [ReactiveFormsModule],
})
export class LoginComponent {
    fb = inject(FormBuilder);

    form = this.fb.nonNullable.group({
        email: ["", Validators.required],
        password: ["", Validators.required]
    });

    onSubmit(): void {
        console.log("login");
    }
}