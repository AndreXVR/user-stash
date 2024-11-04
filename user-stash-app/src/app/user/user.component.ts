import { HttpClient } from "@angular/common/http";
import { Component, inject } from "@angular/core";
import { ReactiveFormsModule, FormBuilder, Validators } from "@angular/forms";
import { UserInterface } from "../user.interface";
import { Router } from "@angular/router";
import { environment } from "../environment";
import { AuthService } from "../auth.service";

@Component({
    selector: "app-user",
    templateUrl: "./user.component.html",
    standalone: true,
    imports: [ReactiveFormsModule],
})
export class UserComponent {
    fb = inject(FormBuilder);
    http = inject(HttpClient);
    authService = inject(AuthService);
    router = inject(Router);

    ngOnInit(): void {
        this.http.get<{user: UserInterface}>(environment.apiUrl + "/api/user").subscribe({
          next: (response) => {
            this.authService.currentUserSig.set(response.user);
          },
          error: () => {
            this.authService.currentUserSig.set(null);
          }
        })
    }

    form = this.fb.nonNullable.group({
        first_name: [this.authService.currentUserSig()?.first_name, Validators.required],
        last_name: [this.authService.currentUserSig()?.last_name, Validators.required],
        email: [this.authService.currentUserSig()?.email, Validators.required],
        old_password: ["", Validators.required],
        new_password: ["", Validators.required],
    });

    onSubmit(): void {
        this.http.post<{user: UserInterface}>(
            environment.apiUrl + "/api/user/update", {
                user: this.form.getRawValue()
            }
        ).subscribe({
            next: (response) => {
                localStorage.setItem("token", response.user.token);
                this.authService.currentUserSig.set(response.user);
                this.router.navigateByUrl("/");
            },
            error: (response) =>{
            alert(response.error);
            }
        });
    }
}