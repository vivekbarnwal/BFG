import { Component } from '@angular/core';
import { NavController } from 'ionic-angular';
import { FormBuilder, FormGroup, Validators } from '@angular/forms';
/* import { EditorModule } from '@tinymce/tinymce-angular'; */

@Component({
  selector: 'page-home',
  templateUrl: 'home.html'
})

export class HomePage {

  // Form group variable
  form: FormGroup;
  selectOptions:any;

  constructor(public navCtrl: NavController, public formBuilder: FormBuilder) {
    // Form control name with default value and validator
    this.form = formBuilder.group({
      option: ['1', Validators.required]
    });
    this.selectOptions = {
      cssClass: 'remove-ok'
    };
  } // constructor()

  submitForm(event): void {
  // Prevent default submit action
  event.preventDefault();

  // Push view to ResultPage with form values
  /* this.navCtrl.push(ResultPage, {
    form: this.form.value
  }); */
  } // submitForm(event)

  ngOnInit() {
    /* let root = this.viewController.instance.navCtrl._app._appRoot;
    document.addEventListener('click', function(event){
    let btn = <HTMLLIElement> document.querySelector('.remove-ok .alert-button-default:nth-child(2)');
    let target = <HTMLElement> event.target;
    if(btn && target.className == 'alert-radio-label')
    {
          let view = root._overlayPortal._views[0];
          let inputs = view.instance.d.inputs;
          for(let input of inputs) {
            if(input.checked) {
              view.instance.d.buttons[1].handler([input.value]);
              view.dismiss();
              break;
            }
          }
        }
    }); */
}

}
