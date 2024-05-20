// red-layer.service.ts
import { Injectable } from '@angular/core';
import { BehaviorSubject } from 'rxjs';

interface LayerVisibility {
  [key: string]: boolean;
}

@Injectable({
  providedIn: 'root'
})
export class LayerVisibilityService {
  private _layerVisibility: LayerVisibility = {
    red: true,
    navy: true,
    green: true,
    black: true
  };

  layerVisibility$ = new BehaviorSubject<LayerVisibility>(this._layerVisibility);

  constructor() {}

  toggleVisibility(layer: string): void {
    this._layerVisibility[layer] = !this._layerVisibility[layer];
    this.layerVisibility$.next({...this._layerVisibility});
  }
}
