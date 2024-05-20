import { ComponentFixture, TestBed } from '@angular/core/testing';

import { Legend2Component } from './legend2.component';

describe('Legend2Component', () => {
  let component: Legend2Component;
  let fixture: ComponentFixture<Legend2Component>;

  beforeEach(() => {
    TestBed.configureTestingModule({
      declarations: [Legend2Component]
    });
    fixture = TestBed.createComponent(Legend2Component);
    component = fixture.componentInstance;
    fixture.detectChanges();
  });

  it('should create', () => {
    expect(component).toBeTruthy();
  });
});
