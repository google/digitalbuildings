package www.google.com.digitalbuildings._0_0_1.fields;

import org.eclipse.rdf4j.model.IRI;
import java.util.Set;
import www.google.com.digitalbuildings._0_0_1.subfields.IPercentage;
import www.google.com.digitalbuildings._0_0_1.subfields.IAir;
import www.google.com.digitalbuildings._0_0_1.subfields.IDamper;
import www.google.com.digitalbuildings._0_0_1.subfields.IOutside;
import www.google.com.digitalbuildings._0_0_1.subfields.ISensor;

public interface IOutside_air_damper_percentage_sensor extends IField{

	public IRI iri();

    public void addComposedOfAir (IAir parameter);

	public Set<IAir> getComposedOfAir();

    public void addComposedOfDamper (IDamper parameter);

	public Set<IDamper> getComposedOfDamper();

    public void addComposedOfOutside (IOutside parameter);

	public Set<IOutside> getComposedOfOutside();

    public void addComposedOfPercentage (IPercentage parameter);

	public Set<IPercentage> getComposedOfPercentage();

    public void addComposedOfSensor (ISensor parameter);

	public Set<ISensor> getComposedOfSensor();

}