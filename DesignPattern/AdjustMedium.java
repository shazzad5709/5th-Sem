public class AdjustMedium implements AdjustColorIntensity{
    protected String tonerSavingLevel;
    protected String colorIntensity;
    @Override
    public void adjustColorIntensity() {
         if(tonerSavingLevel=="medium"){
            colorIntensity="modarately reduced";
        }
    }
}
