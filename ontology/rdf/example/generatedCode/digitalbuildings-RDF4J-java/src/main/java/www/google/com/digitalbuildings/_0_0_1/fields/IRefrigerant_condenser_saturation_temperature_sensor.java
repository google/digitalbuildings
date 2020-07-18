package www.google.com.digitalbuildings._0_0_1.fields;

import org.eclipse.rdf4j.model.IRI;
import java.util.Set;
import www.google.com.digitalbuildings._0_0_1.subfields.ITemperature;
import www.google.com.digitalbuildings._0_0_1.subfields.ICondenser;
import www.google.com.digitalbuildings._0_0_1.subfields.IRefrigerant;
import www.google.com.digitalbuildings._0_0_1.subfields.ISaturation;
import www.google.com.digitalbuildings._0_0_1.subfields.ISensor;

public interface IRefrigerant_condenser_saturation_temperature_sensor extends IField{

	public IRI iri();

    public void addComposedOfCondenser (ICondenser parameter);

	public Set<ICondenser> getComposedOfCondenser();

    public void addComposedOfRefrigerant (IRefrigerant parameter);

	public Set<IRefrigerant> getComposedOfRefrigerant();

    public void addComposedOfSaturation (ISaturation parameter);

	public Set<ISaturation> getComposedOfSaturation();

    public void addComposedOfSensor (ISensor parameter);

	public Set<ISensor> getComposedOfSensor();

    public void addComposedOfTemperature (ITemperature parameter);

	public Set<ITemperature> getComposedOfTemperature();

}