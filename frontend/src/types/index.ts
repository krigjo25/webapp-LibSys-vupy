export interface Review {
    name?: string;
    rating?: number;
}

export interface Book {
    bookID?: string;
    title: string;
    author: string;
    year?: string;
    genre: string[];
    description: string;
    published_by?: string;
    path?: string;
    reviews: Review;
}

export interface ActionButtonData {
    type: 'button' | 'submit' | 'reset';
    action: (book?: any) => void;
    cls: string;
    name: string;
}

export type NavigationData = ActionButtonData[];

export interface InputFieldData {
    name: string;
    type: string;
    placeholder?: string | number;
    value: any;
}

export interface FormConfig {
    title: string;
    bookid: string | null;
    data: InputFieldData[];
}
