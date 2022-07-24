## Basic Implementation for react

``` javascript
import React from 'react'

const Form = () => {
    const data:Data = {
        Name : formData['user']['name'] ,
        Email : formData['user']['email'],
        Pregnancies : formData['user']['pregnancy'],
        Glucose  : formData['user']['glucose'],
        BloodPressure  : formData['user']['pressure'],
        SkinThickness  : formData['user']['thickness'],
        Insulin  : formData['user']['insulin'],
        BMI  : formData['user']['bmi'],
        DiabetesPedigreeFunction  : formData['family']['states'][0],
	    Age:formData['user']['age']
    }

    const onSubmit = (e: FormEvent) => {
        e.preventDefault()
        makeDiagnosis()
    }

    let makeDiagnosis = async () => {
        fetch(`https://newdiabetesapi.herokuapp.com/api/users/diagnosis/`, {
            method:'POST',
            headers:{
                'Content-Type':'application/json',
            },
            body:JSON.stringify(data)
        })
    }    


  return (
    <form onSubmit={onSubmit}>
      {
        forms.map((form, index)=>(
          <div key={index}>
            <label'>{form.label}</label>
            <input onChange={onInputChange} type={form.type} name={form.name}/>
          </div>  
        ))
      } 
      <label>Do you have any known family history of diabetes? (Required)</label>
      <div>
        <div>
            <input
                type="radio"
                value="1"
                name='states'
                onChange={onSelectChange}
                className='mr-4'
            />
            <label>Yes I do</label>
        </div>
        <div>
            <input
                type="radio"
                value= '0'
                name='states'
                onChange={onSelectChange}
            />
            <label>No I do not</label>
        </div>
      </div>
     
      <div><button type="submit">Submit</button></div>
    </form>
  )
}

export default Form
```
