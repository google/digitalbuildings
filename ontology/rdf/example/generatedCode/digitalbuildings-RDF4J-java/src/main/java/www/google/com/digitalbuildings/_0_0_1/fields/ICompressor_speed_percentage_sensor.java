package www.google.com.digitalbuildings._0_0_1.fields;

import org.eclipse.rdf4j.model.IRI;
import java.util.Set;
import www.google.com.digitalbuildings._0_0_1.subfields.ISpeed;
import www.google.com.digitalbuildings._0_0_1.subfields.IPercentage;
import www.google.com.digitalbuildings._0_0_1.subfields.ICompressor;
import www.google.com.digitalbuildings._0_0_1.subfields.ISensor;

public interface ICompressor_speed_percentage_sensor extends IField{

	public IRI iri();

    public void addComposedOfCompressor (ICompressor parameter);

	public Set<ICompressor> getComposedOfCompressor();

    public void addComposedOfPercentage (IPercentage parameter);

	public Set<IPercentage> getComposedOfPercentage();

    public void addComposedOfSensor (ISensor parameter);

	public Set<ISensor> getComposedOfSensor();

    public void addComposedOfSpeed (ISpeed parameter);

	public Set<ISpeed> getComposedOfSpeed();

}