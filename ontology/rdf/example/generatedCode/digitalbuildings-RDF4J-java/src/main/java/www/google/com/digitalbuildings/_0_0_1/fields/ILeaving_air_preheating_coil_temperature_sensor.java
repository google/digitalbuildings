package www.google.com.digitalbuildings._0_0_1.fields;

import org.eclipse.rdf4j.model.IRI;
import java.util.Set;
import www.google.com.digitalbuildings._0_0_1.subfields.ITemperature;
import www.google.com.digitalbuildings._0_0_1.subfields.ILeaving;
import www.google.com.digitalbuildings._0_0_1.subfields.IAir;
import www.google.com.digitalbuildings._0_0_1.subfields.IPreheating;
import www.google.com.digitalbuildings._0_0_1.subfields.ICoil;
import www.google.com.digitalbuildings._0_0_1.subfields.ISensor;

public interface ILeaving_air_preheating_coil_temperature_sensor extends IField{

	public IRI iri();

    public void addComposedOfAir (IAir parameter);

	public Set<IAir> getComposedOfAir();

    public void addComposedOfCoil (ICoil parameter);

	public Set<ICoil> getComposedOfCoil();

    public void addComposedOfLeaving (ILeaving parameter);

	public Set<ILeaving> getComposedOfLeaving();

    public void addComposedOfPreheating (IPreheating parameter);

	public Set<IPreheating> getComposedOfPreheating();

    public void addComposedOfSensor (ISensor parameter);

	public Set<ISensor> getComposedOfSensor();

    public void addComposedOfTemperature (ITemperature parameter);

	public Set<ITemperature> getComposedOfTemperature();

}